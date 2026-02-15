"""
Optional PDF export for pipeline results.

Uses reportlab when available; logs warning and skips if not installed.
"""

import logging
from datetime import datetime
from pathlib import Path
from typing import TYPE_CHECKING

from core.diagnostics import Diagnostic

if TYPE_CHECKING:
    from main import PipelineResult, ExportOptions

logger = logging.getLogger(__name__)

try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import (
        SimpleDocTemplate,
        Paragraph,
        Spacer,
        Table,
        TableStyle,
        PageBreak,
        Preformatted,
    )
    HAS_REPORTLAB = True
except ImportError:
    HAS_REPORTLAB = False


def export_pipeline_result_to_pdf(
    result: "PipelineResult",
    export: "ExportOptions",
) -> str:
    """
    Render key information (AST summaries, diagnostics, stats) into a PDF.

    Returns the path of the generated PDF.
    """
    if not HAS_REPORTLAB:
        logger.warning("reportlab not installed; skipping PDF export")
        raise ImportError("reportlab is required for PDF export. Install with: pip install reportlab")

    pdf_path = export.pdf_path
    if not pdf_path:
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        pdf_path = f"report_{ts}.pdf"
    pdf_path = Path(pdf_path)
    pdf_path.parent.mkdir(parents=True, exist_ok=True)

    doc = SimpleDocTemplate(str(pdf_path), pagesize=letter, rightMargin=inch, leftMargin=inch)
    styles = getSampleStyleSheet()
    flow: list = []

    # Title
    flow.append(Paragraph("IBM i Artifact Analysis Report", styles["Title"]))
    flow.append(Spacer(1, 0.2 * inch))

    # Metadata
    flow.append(Paragraph("Run Metadata", styles["Heading2"]))
    meta = [
        ["Timestamp", datetime.now().isoformat()],
        ["Total diagnostics", str(len(result.diagnostics))],
        ["CL files", str(len(result.cl_results))],
        ["RPG files", str(len(result.rpg_results))],
        ["DB2 files", str(len(result.db2_results))],
        ["DSPF files", str(len(result.dspf_results))],
    ]
    t = Table(meta)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), colors.lightgrey),
        ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
    ]))
    flow.append(t)
    flow.append(Spacer(1, 0.3 * inch))

    # Per-module summaries
    flow.append(Paragraph("Module Summaries", styles["Heading2"]))
    
    # Style for code blocks
    code_style = ParagraphStyle('Code', parent=styles['Normal'], fontName='Courier', fontSize=8, leading=10)

    def add_module_report(title: str, res: object):
        flow.append(Paragraph(f"{title}: {res.path}", styles["Heading3"]))
        
        # Add AST tree if available
        if hasattr(res, "ast_tree") and res.ast_tree:
            flow.append(Paragraph("AST Structure", styles["Heading4"]))
            flow.append(Preformatted(res.ast_tree, code_style))
            flow.append(Spacer(1, 0.1 * inch))
        
        if hasattr(res, "summary_report") and res.summary_report:
            flow.append(Paragraph("Analysis Report", styles["Heading4"]))
            flow.append(Preformatted(res.summary_report, code_style))
        else:
            flow.append(Paragraph("No detailed report available.", styles["Normal"]))
        flow.append(Spacer(1, 0.2 * inch))

    for r in result.cl_results:
        add_module_report("CL", r)
    for r in result.rpg_results:
        add_module_report("RPG", r)
    for r in result.db2_results:
        add_module_report("DB2", r)
    for r in result.dspf_results:
        add_module_report("DSPF", r)
    flow.append(Spacer(1, 0.3 * inch))

    # Diagnostics
    flow.append(Paragraph("Diagnostics", styles["Heading2"]))
    if result.diagnostics:
        diag_data = [["File", "Line", "Col", "Severity", "Message"]]
        for d in result.diagnostics[:100]:  # cap at 100
            diag_data.append([str(d.file), str(d.line), str(d.column), d.severity, d.message[:80]])
        t2 = Table(diag_data)
        t2.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ("FONTSIZE", (0, 0), (-1, -1), 8),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ]))
        flow.append(t2)
        if len(result.diagnostics) > 100:
            flow.append(Paragraph(f"... and {len(result.diagnostics) - 100} more", styles["Normal"]))
    else:
        flow.append(Paragraph("No diagnostics.", styles["Normal"]))

    doc.build(flow)
    return str(pdf_path)
