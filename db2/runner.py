"""
DB2 SQL runner: parse file and return Db2Result.
"""

from dataclasses import dataclass, field
from typing import List, Optional

from core.diagnostics import Diagnostic
from core.io import load_file
from db2.ast_nodes import Db2Script, Db2Ddl
from db2.ast_builder import parse_db2

@dataclass
class Db2Metrics:
    table_count: int = 0
    column_count: int = 0
    index_count: int = 0
    complexity: str = "Low"

@dataclass
class Db2Result:
    """Result of running DB2 parser on a file."""

    path: str
    ast: Optional[Db2Script]
    diagnostics: List[Diagnostic]
    metrics: Db2Metrics = field(default_factory=Db2Metrics)
    summary_report: str = ""
    ast_tree: str = ""


def run_db2_file(path: str) -> Db2Result:
    """
    Parses a DB2 SQL file and generates a summarization report.
    """
    try:
        source = load_file(path)
    except Exception as e:
        return Db2Result(path, None, [Diagnostic(path, 0, 0, "error", str(e))])

    ast, parse_diag = parse_db2(source, path)
    diagnostics = parse_diag
    
    # AST Generation
    ast_lines = []
    ast_lines.append("AST Representation")

    def dump_ast(node, parent_prefix="", is_last_child=False):
        if isinstance(node, Db2Script):
            ast_lines.append("Db2Script")
            for i, stmt in enumerate(node.statements):
                is_last_stmt = (i == len(node.statements) - 1)
                dump_ast(stmt, "", is_last_stmt)
        elif isinstance(node, Db2Ddl):
            connector = "└── " if is_last_child else "├── "
            ast_lines.append(f"{parent_prefix}{connector}{node.kind}: {node.name}")
        else:
            connector = "└── " if is_last_child else "├── "
            stmt_type = type(node).__name__.replace("Db2", "")
            ast_lines.append(f"{parent_prefix}{connector}Statement: {stmt_type}")

    if ast:
        dump_ast(ast)
    else:
        ast_lines.append("  (No AST generated)")

    metrics = Db2Metrics()
    ops = set()
    if ast:
        # Count CREATE TABLE statements
        tables = [s for s in ast.statements if isinstance(s, Db2Ddl) and s.kind == "CREATE TABLE"]
        metrics.table_count = len(tables)
        metrics.column_count = 0 # Column parsing requires deeper DDL analysis not yet in AST
        # Mock index count for now
        metrics.index_count = 0
        for s in ast.statements:
            if isinstance(s, Db2Ddl): ops.add(s.kind)
            else: ops.add("DML")

    # Generate Text Report
    lines = []
    lines.append("Summarization/Analysis Report")
    lines.append(f"File: {path}")
    lines.append("Type: DB2 SQL")
    lines.append("I. Overview")
    lines.append(f"Total Lines: {len(source.splitlines())}")
    lines.append(f"Logical LOC: {len(ast.statements) if ast else 0}")
    lines.append(f"Procedural Complexity: Low (Declarative)")
    lines.append(f"Type of Operations: {', '.join(ops) if ops else 'None'}")
    lines.append("II. Metrics & Violations")
    lines.append(f"Maintainability Index: High")
    lines.append(f"Issues: {len(diagnostics)}")
    lines.append("III. Data Flow & Dependencies")
    lines.append(f"Tables Defined: {metrics.table_count}")
    
    report_text = "\n".join(lines)

    return Db2Result(path, ast, diagnostics, metrics, report_text, "\n".join(ast_lines))
