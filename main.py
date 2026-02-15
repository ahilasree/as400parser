"""
Central dispatcher for IBM i artifact parsing pipeline.

Takes input describing which artifact(s) to run, invokes specific module(s)
or a combined pipeline, and returns PipelineResult.
"""

import argparse
from dataclasses import dataclass, field
from pathlib import Path

from core.config import infer_kind_from_path, infer_kind_from_content
from core.diagnostics import Diagnostic
from core.io import load_file, discover_files


@dataclass
class InputSpec:
    """Input specification for a single artifact."""

    path: str
    kind: str  # "cl", "rpg", "db2", "dspf", or "auto"


@dataclass
class PipelineResult:
    """Aggregated result from run_pipeline."""

    cl_results: list["ClResult"]
    rpg_results: list["RpgResult"]
    db2_results: list["Db2Result"]
    dspf_results: list["DspfResult"]
    diagnostics: list[Diagnostic] = field(default_factory=list)


# Import runners lazily to avoid circular deps
def _run_cl(path: str) -> "ClResult":
    from cl.runner import run_cl_file

    return run_cl_file(path)


def _run_rpg(path: str) -> "RpgResult":
    from rpg.runner import run_rpg_file

    return run_rpg_file(path)


def _run_db2(path: str) -> "Db2Result":
    from db2.runner import run_db2_file

    return run_db2_file(path)


def _run_dspf(path: str) -> "DspfResult":
    from dspf.runner import run_dspf_file

    return run_dspf_file(path)


def run_pipeline(
    inputs: list[InputSpec],
    mode: str = "auto",
    export: "ExportOptions | None" = None,
) -> PipelineResult:
    """
    Run the parsing pipeline on the given inputs.

    Args:
        inputs: List of InputSpec (path + kind).
        mode: "cl" | "rpg" | "db2" | "dspf" | "combined" | "auto".
        export: Optional ExportOptions for PDF/email export.

    Returns:
        PipelineResult with ASTs, diagnostics, and optional cross-links.
    """
    cl_results: list = []
    rpg_results: list = []
    db2_results: list = []
    dspf_results: list = []
    all_diagnostics: list[Diagnostic] = []

    for spec in inputs:
        kind = spec.kind if spec.kind != "auto" else infer_kind_from_path(spec.path)
        if kind == "auto":
            try:
                content = load_file(spec.path)
                kind = infer_kind_from_content(content, spec.path)
            except Exception:
                kind = infer_kind_from_path(spec.path)

        # combined/auto: run module matching inferred kind per file
        # cl/rpg/db2/dspf: run only that module on matching inputs
        run_cl = (mode in ("cl", "combined", "auto") and kind in ("cl", "auto"))
        run_rpg = (mode in ("rpg", "combined", "auto") and kind in ("rpg", "auto"))
        run_db2 = (mode in ("db2", "combined", "auto") and kind in ("db2", "auto"))
        run_dspf = (mode in ("dspf", "combined", "auto") and kind in ("dspf", "auto"))
        if mode == "cl":
            run_cl = kind in ("cl", "auto")
            run_rpg = run_db2 = run_dspf = False
        if mode == "rpg":
            run_rpg = kind in ("rpg", "auto")
            run_cl = run_db2 = run_dspf = False
        if mode == "db2":
            run_db2 = kind in ("db2", "auto")
            run_cl = run_rpg = run_dspf = False
        if mode == "dspf":
            run_dspf = kind in ("dspf", "auto")
            run_cl = run_rpg = run_db2 = False

        if run_cl:
            r = _run_cl(spec.path)
            cl_results.append(r)
            all_diagnostics.extend(r.diagnostics)
        if run_rpg:
            r = _run_rpg(spec.path)
            rpg_results.append(r)
            all_diagnostics.extend(r.diagnostics)
        if run_db2:
            r = _run_db2(spec.path)
            db2_results.append(r)
            all_diagnostics.extend(r.diagnostics)
        if run_dspf:
            r = _run_dspf(spec.path)
            dspf_results.append(r)
            all_diagnostics.extend(r.diagnostics)

    result = PipelineResult(
        cl_results=cl_results,
        rpg_results=rpg_results,
        db2_results=db2_results,
        dspf_results=dspf_results,
        diagnostics=all_diagnostics,
    )

    # Optional PDF export
    if export is not None and export.enable_pdf:
        try:
            from core.export_pdf import export_pipeline_result_to_pdf

            pdf_path = export_pipeline_result_to_pdf(result, export)
            if export.enable_email and pdf_path and export.email_to and export.email_smtp_config:
                from core.emailer import send_pipeline_pdf_via_email

                send_pipeline_pdf_via_email(pdf_path, export)
        except Exception as e:
            result.diagnostics.append(
                Diagnostic(
                    file="<pipeline>",
                    line=0,
                    column=0,
                    severity="warning",
                    message=f"Export failed: {e}",
                )
            )

    return result


@dataclass
class ExportOptions:
    """Options for PDF/email export."""

    enable_pdf: bool = False
    pdf_path: str | None = None
    enable_email: bool = False
    email_to: str | None = None
    email_subject: str | None = None
    email_smtp_config: dict | None = None  # host, port, username, password, use_tls


# Type hints for PipelineResult (avoid import at parse time)
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cl.runner import ClResult
    from rpg.runner import RpgResult
    from db2.runner import Db2Result
    from dspf.runner import DspfResult


def main_cli() -> None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="IBM i artifact parser and analyzer")
    parser.add_argument("files", nargs="*", help="Input files (CL, RPG, DB2, DSPF)")
    parser.add_argument(
        "--mode",
        choices=["auto", "cl", "rpg", "db2", "dspf", "combined"],
        default="combined",
        help="Pipeline mode",
    )
    parser.add_argument("--export-pdf", type=str, default=None, help="Export PDF to path")
    parser.add_argument("--email-to", type=str, default=None, help="Email address for report")
    parser.add_argument("--email-subject", type=str, default="IBM i analysis report", help="Email subject")
    parser.add_argument("--smtp-host", type=str, default=None, help="SMTP host")
    parser.add_argument("--smtp-port", type=int, default=587, help="SMTP port")
    parser.add_argument("--smtp-user", type=str, default=None, help="SMTP username")
    parser.add_argument("--smtp-pass", type=str, default=None, help="SMTP password")
    parser.add_argument("--smtp-tls", action="store_true", help="Use TLS for SMTP")
    args = parser.parse_args()

    inputs = [InputSpec(path=f, kind="auto") for f in args.files]
    if not inputs:
        print("No files specified. Use: python main.py --mode combined prog.clle prog.rpgle schema.sql display.dspf")
        return

    export = None
    if args.export_pdf or args.email_to:
        smtp_config = None
        if args.smtp_host and args.email_to:
            smtp_config = {
                "host": args.smtp_host,
                "port": args.smtp_port,
                "username": args.smtp_user,
                "password": args.smtp_pass,
                "use_tls": args.smtp_tls,
            }
        export = ExportOptions(
            enable_pdf=bool(args.export_pdf),
            pdf_path=args.export_pdf,
            enable_email=bool(args.email_to),
            email_to=args.email_to,
            email_subject=args.email_subject or "IBM i Analysis Report",
            email_smtp_config=smtp_config,
        )

    result = run_pipeline(inputs, mode=args.mode, export=export)
    print(f"Pipeline completed. Diagnostics: {len(result.diagnostics)}")
    for d in result.diagnostics[:20]:
        print(f"  {d}")
    if len(result.diagnostics) > 20:
        print(f"  ... and {len(result.diagnostics) - 20} more")
    print(f"CL: {len(result.cl_results)}, RPG: {len(result.rpg_results)}, DB2: {len(result.db2_results)}, DSPF: {len(result.dspf_results)}")
    print("\n--- Analysis Reports ---")
    for r in result.cl_results:
        print(f"\n{r.summary_report}")
    for r in result.rpg_results:
        print(f"\n{r.summary_report}")
    for r in result.db2_results:
        print(f"\n{r.summary_report}")
    for r in result.dspf_results:
        print(f"\n{r.summary_report}")
    
    # Optionally print mermaid diagrams if they exist
    print("\n--- Mermaid Diagrams (for rendering in a compatible viewer) ---")
    for r in result.rpg_results:
        if hasattr(r, 'mermaid_diagram') and r.mermaid_diagram:
            print(f"\n--- Diagram for {r.path} ---\n```mermaid\n{r.mermaid_diagram}\n```")


if __name__ == "__main__":
    main_cli()
