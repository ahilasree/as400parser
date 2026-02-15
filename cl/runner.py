"""
CL/CLLE runner: parse file and return ClResult with AST and diagnostics.
"""

from dataclasses import dataclass, field
from typing import List, Optional

from core.diagnostics import Diagnostic
from core.io import load_file
from cl.ast_nodes import ClProgram, ClCommand
from cl.ast_builder import parse_cl

@dataclass
class ClMetrics:
    command_count: int = 0
    variable_count: int = 0
    cyclomatic_complexity: int = 1
    maintainability_rating: str = "A"

@dataclass
class ClResult:
    """Result of running CL parser on a file."""

    path: str
    ast: Optional[ClProgram]
    diagnostics: List[Diagnostic]
    metrics: ClMetrics = field(default_factory=ClMetrics)
    summary_report: str = ""
    ast_tree: str = ""


def run_cl_file(path: str) -> ClResult:
    """
    Parse a CL/CLLE file and return ClResult.
    """
    try:
        source = load_file(path)
    except Exception as e:
        return ClResult(path, None, [Diagnostic(path, 0, 0, "error", str(e))])

    ast, parse_diag = parse_cl(source, path)
    diagnostics = parse_diag

    # AST Generation
    ast_lines = []
    ast_lines.append("AST Representation")

    def dump_ast(node, indent=0, is_last_child=False, parent_prefix=""):
        if isinstance(node, ClProgram):
            ast_lines.append("ClProgram")
            for i, command in enumerate(node.commands):
                is_last = (i == len(node.commands) - 1)
                dump_ast(command, 1, is_last, "")
        elif isinstance(node, ClCommand):
            connector = "└── " if is_last_child else "├── "
            current_prefix = parent_prefix + connector
            ast_lines.append(f"{parent_prefix}{connector}Command: {node.name}")
            
            # Build prefix for children
            child_prefix = parent_prefix + ("    " if is_last_child else "│   ")
            
            for i, param in enumerate(node.parameters):
                is_last_param = (i == len(node.parameters) - 1)
                param_connector = "└── " if is_last_param else "├── "
                if param.keyword:
                    ast_lines.append(f"{child_prefix}{param_connector}Parameter: {param.keyword}={param.value.text}")
                else:
                    ast_lines.append(f"{child_prefix}{param_connector}Parameter: {param.value.text}")

    if ast:
        dump_ast(ast)
    else:
        ast_lines.append("  (No AST generated)")

    metrics = ClMetrics()
    unique_ops = set()
    files_used = set()
    internal_vars = []

    if ast:
        metrics.command_count = len(ast.commands)
        metrics.variable_count = len([c for c in ast.commands if c.name == 'DCL'])
        
        # Rough complexity: +1 for IF, DOFOR, DOWHILE, MONMSG
        for cmd in ast.commands:
            unique_ops.add(cmd.name)
            if cmd.name in ('IF', 'DOFOR', 'DOWHILE', 'MONMSG'):
                metrics.cyclomatic_complexity += 1
            if cmd.name == 'DCLF':
                files_used.add("Declared File") # Simplified extraction
            if cmd.name == 'DCL':
                internal_vars.append("Variable") # Simplified extraction

    # Generate Text Report
    lines = []
    lines.append("Summarization/Analysis Report")
    lines.append(f"Program: {path}")
    lines.append("Type: CL/CLLE")
    lines.append("I. Overview")
    lines.append(f"Total Lines: {len(source.splitlines())}")
    lines.append(f"Logical LOC: {metrics.command_count}")
    lines.append(f"Procedural Complexity: {'Low' if metrics.cyclomatic_complexity < 5 else 'Medium'} ({metrics.cyclomatic_complexity})")
    lines.append(f"Database Access: {len(files_used)} Files")
    lines.append(f"Type of Operations: {', '.join(sorted(list(unique_ops))) if unique_ops else 'None'}")
    lines.append("II. Metrics & Violations")
    lines.append(f"Maintainability Index: {metrics.maintainability_rating}")
    lines.append(f"Cyclomatic Complexity: {metrics.cyclomatic_complexity}")
    lines.append(f"Issues: {len(diagnostics)}")
    lines.append("III. Data Flow & Dependencies")
    lines.append(f"Files Used: {', '.join(files_used) if files_used else 'None'}")
    lines.append(f"Internal Variables: {metrics.variable_count} defined")
    
    report_text = "\n".join(lines)

    return ClResult(path, ast, diagnostics, metrics, report_text, "\n".join(ast_lines))
