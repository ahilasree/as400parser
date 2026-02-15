"""
Example usage of per-language runners and run_pipeline.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

EXAMPLES = ROOT / "examples"


def main():
    from main import run_pipeline, InputSpec

    print("=== Per-language runners ===\n")

    # CL
    cl_path = EXAMPLES / "example.clle"
    if cl_path.exists():
        from cl.runner import run_cl_file
        r = run_cl_file(str(cl_path))
        print(f"CL: {r.path}, commands={len(r.ast.commands) if r.ast else 0}, diag={len(r.diagnostics)}")
        if r.ast:
            for cmd in r.ast.commands[:3]:
                print(f"  - {cmd.name}")

    # RPG
    rpg_path = EXAMPLES / "example.rpgle"
    if rpg_path.exists():
        from rpg.runner import run_rpg_file
        r = run_rpg_file(str(rpg_path))
        print(f"\nRPG: {r.path}, procedures={len(r.ast.procedures) if r.ast else 0}, sql={len(r.ast.sql_statements) if r.ast else 0}, diag={len(r.diagnostics)}")

    # DB2
    db2_path = EXAMPLES / "schema.sql"
    if db2_path.exists():
        from db2.runner import run_db2_file
        r = run_db2_file(str(db2_path))
        print(f"\nDB2: {r.path}, statements={len(r.ast.statements) if r.ast else 0}, diag={len(r.diagnostics)}")

    # DSPF
    dspf_path = EXAMPLES / "display.dspf"
    if dspf_path.exists():
        from dspf.runner import run_dspf_file
        r = run_dspf_file(str(dspf_path))
        print(f"\nDSPF: {r.path}, records={len(r.ast.record_formats) if r.ast else 0}, diag={len(r.diagnostics)}")

    print("\n=== run_pipeline (combined) ===\n")
    inputs = [
        InputSpec(path=str(EXAMPLES / "example.clle"), kind="cl"),
        InputSpec(path=str(EXAMPLES / "example.rpgle"), kind="rpg"),
        InputSpec(path=str(EXAMPLES / "schema.sql"), kind="db2"),
        InputSpec(path=str(EXAMPLES / "display.dspf"), kind="dspf"),
    ]
    result = run_pipeline(inputs, mode="combined")
    print(f"Pipeline: CL={len(result.cl_results)}, RPG={len(result.rpg_results)}, DB2={len(result.db2_results)}, DSPF={len(result.dspf_results)}")
    print(f"Diagnostics: {len(result.diagnostics)}")
    for d in result.diagnostics[:5]:
        print(f"  {d}")


if __name__ == "__main__":
    main()
