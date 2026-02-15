"""
DSPF DDS runner: parse file and return DspfResult.
"""

from dataclasses import dataclass, field
from typing import List, Optional
from core.diagnostics import Diagnostic
from core.io import load_file
from dspf.ast_nodes import DisplayFile
from dspf.ast_builder import parse_dspf

@dataclass
class DspfMetrics:
    record_count: int = 0
    field_count: int = 0
    screen_size: str = "24x80"

@dataclass
class DspfResult:
    path: str
    ast: Optional[DisplayFile]
    diagnostics: List[Diagnostic]
    metrics: DspfMetrics = field(default_factory=DspfMetrics)
    summary_report: str = ""
    ast_tree: str = ""

def run_dspf_file(path: str) -> DspfResult:
    """
    Parses a DSPF file and generates a summarization report.
    """
    try:
        source = load_file(path)
    except Exception as e:
        return DspfResult(path, None, [Diagnostic(path, 0, 0, "error", str(e))])

    ast, diagnostics = parse_dspf(source, path)
    
    # AST Generation
    ast_lines = []
    ast_lines.append("AST Representation")

    def dump_ast(node, parent_prefix="", is_last_child=False):
        if isinstance(node, DisplayFile):
            ast_lines.append("DisplayFile")
            for i, r in enumerate(node.record_formats):
                is_last_record = (i == len(node.record_formats) - 1)
                dump_ast(r, "", is_last_record)
        elif hasattr(node, "fields") and hasattr(node, "name"):
            connector = "└── " if is_last_child else "├── "
            ast_lines.append(f"{parent_prefix}{connector}Record: {node.name}")
            record_prefix = parent_prefix + ("    " if is_last_child else "│   ")
            for i, f in enumerate(node.fields):
                is_last_field = (i == len(node.fields) - 1)
                dump_ast(f, record_prefix, is_last_field)
        elif hasattr(node, "length") and hasattr(node, "name"):
            connector = "└── " if is_last_child else "├── "
            dtype = getattr(node, "data_type", "") or ""
            ast_lines.append(f"{parent_prefix}{connector}Field: {node.name} ({dtype} {node.length})")

    if ast:
        dump_ast(ast)
    else:
        ast_lines.append("  (No AST generated)")

    metrics = DspfMetrics()
    if ast:
        metrics.record_count = len(ast.record_formats)
        metrics.field_count = sum(len(r.fields) for r in ast.record_formats)

    # Generate Report
    lines = []
    lines.append("Summarization/Analysis Report")
    lines.append(f"File: {path}")
    lines.append("Type: DSPF (DDS)")
    lines.append("I. Overview")
    lines.append(f"Total Lines: {len(source.splitlines())}")
    lines.append(f"Logical LOC: {metrics.record_count + metrics.field_count}")
    lines.append(f"Procedural Complexity: Low (Declarative)")
    lines.append(f"Type of Operations: Record Definition, Field Definition")
    lines.append("II. Metrics & Violations")
    lines.append(f"Maintainability Index: High")
    lines.append(f"Issues: {len(diagnostics)}")
    lines.append("III. Data Flow & Dependencies")
    lines.append(f"Records: {metrics.record_count}")
    lines.append(f"Fields: {metrics.field_count}")
    
    report_text = "\n".join(lines)

    return DspfResult(path, ast, diagnostics, metrics, report_text, "\n".join(ast_lines))