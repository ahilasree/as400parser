"""
RPG/RPGLE/SQLRPGLE runner: parse file and return RpgResult.
"""

from dataclasses import dataclass, field

from core.diagnostics import Diagnostic
from core.io import load_file
from rpg.ast_nodes import (
    RpgProgram,
    RpgIfStmt,
    RpgSelectStmt,
    RpgDoForStmt,
    RpgProcedure,
    RpgStatement,
    RpgAssignStmt,
    RpgCallStmt,
    RpgReturnStmt,
    EmbeddedSqlStmt,
)
from rpg.ast_builder import parse_rpg


@dataclass
class RpgMetrics:
    cyclomatic_complexity: int = 1
    procedure_count: int = 0
    variable_count: int = 0
    sql_statement_count: int = 0
    maintainability_rating: str = "A"


@dataclass
class RpgResult:
    """Result of running RPG parser on a file."""

    path: str
    ast: RpgProgram | None
    diagnostics: list[Diagnostic]
    metrics: RpgMetrics = field(default_factory=RpgMetrics)
    summary_report: str = ""
    mermaid_diagram: str = ""
    ast_tree: str = ""


def run_rpg_file(path: str) -> RpgResult:
    """Parse an RPG/RPGLE/SQLRPGLE file and return RpgResult."""
    diagnostics: list[Diagnostic] = []
    try:
        source = load_file(path)
    except (FileNotFoundError, UnicodeDecodeError) as e:
        diagnostics.append(
            Diagnostic(file=path, line=0, column=0, severity="error", message=str(e))
        )
        return RpgResult(path=path, ast=None, diagnostics=diagnostics)

    ast, parse_diag = parse_rpg(source, path)
    diagnostics.extend(parse_diag)

    # AST Generation
    ast_lines = []
    ast_lines.append("AST Representation")
    
    mermaid_lines = ["graph TD"]
    node_counter = 0

    def dump_ast_text(node, parent_prefix="", is_last_child=False):
        if isinstance(node, RpgProgram):
            ast_lines.append("RpgProgram")
            # Variables
            if node.variables:
                ast_lines.append(f"{parent_prefix}├── DataDeclarations ({len(node.variables)})")
                var_prefix = parent_prefix + "│   "
                for i, v in enumerate(node.variables):
                    is_last_var = (i == len(node.variables) - 1)
                    var_connector = "└── " if is_last_var else "├── "
                    ast_lines.append(f"{var_prefix}{var_connector}Decl: {v.name} ({v.data_type})")
            # Statements
            ast_lines.append(f"{parent_prefix}└── StatementList")
            stmt_prefix = parent_prefix + "    "
            for i, s in enumerate(node.main_body):
                is_last_stmt = (i == len(node.main_body) - 1)
                dump_ast_text(s, stmt_prefix, is_last_stmt)
            # Procedures
            for p in node.procedures:
                dump_ast_text(p, parent_prefix, False)
        elif isinstance(node, RpgProcedure):
            connector = "└── " if is_last_child else "├── "
            ast_lines.append(f"{parent_prefix}{connector}Procedure: {node.name}")
            proc_prefix = parent_prefix + ("    " if is_last_child else "│   ")
            for i, s in enumerate(node.body):
                is_last_proc_stmt = (i == len(node.body) - 1)
                dump_ast_text(s, proc_prefix, is_last_proc_stmt)
        elif isinstance(node, (RpgAssignStmt, RpgCallStmt, RpgIfStmt, EmbeddedSqlStmt)):
            connector = "└── " if is_last_child else "├── "
            node_type = type(node).__name__.replace("Rpg", "").replace("Stmt", "")
            if isinstance(node, RpgCallStmt):
                ast_lines.append(f"{parent_prefix}{connector}{node_type}: {node.name}")
            elif isinstance(node, EmbeddedSqlStmt):
                ast_lines.append(f"{parent_prefix}{connector}{node_type}: {node.stmt_type}")
            else:
                ast_lines.append(f"{parent_prefix}{connector}{node_type}")
    
    def dump_ast_mermaid(node, parent_id=None):
        nonlocal node_counter
        node_counter += 1
        my_id = f"n{node_counter}"
        node_label = type(node).__name__.replace("Rpg", "").replace("Stmt", "")
        if hasattr(node, 'name'):
            node_label += f": {node.name}"
        mermaid_lines.append(f'{my_id}["{node_label}"]')
        if parent_id:
            mermaid_lines.append(f"{parent_id} --> {my_id}")
        if isinstance(node, RpgProgram):
            for s in node.main_body: dump_ast_mermaid(s, my_id)
            for p in node.procedures: dump_ast_mermaid(p, my_id)
        elif isinstance(node, (RpgProcedure, RpgIfStmt)):
            body = getattr(node, 'body', []) or getattr(node, 'then_body', [])
            for s in body: dump_ast_mermaid(s, my_id)

    if ast:
        dump_ast_text(ast)
        dump_ast_mermaid(ast)
    else:
        ast_lines.append("  (No AST generated)")
        mermaid_lines.append('n1["No AST generated"]')

    metrics = RpgMetrics()
    if ast:
        metrics.procedure_count = len(ast.procedures)
        metrics.variable_count = len(ast.variables)
        metrics.sql_statement_count = len(ast.sql_statements)

        # Calculate Complexity (Base 1 + Control Flow)
        complexity = 1

        def visit_stmts(stmts: list):
            nonlocal complexity
            for stmt in stmts:
                if isinstance(stmt, (RpgIfStmt, RpgSelectStmt, RpgDoForStmt)):
                    complexity += 1
                # Recurse into bodies if they exist (simplified for this AST structure)
                if hasattr(stmt, "then_body"):
                    visit_stmts(stmt.then_body)
                if hasattr(stmt, "else_body"):
                    visit_stmts(stmt.else_body)
                if hasattr(stmt, "body") and isinstance(stmt.body, list):
                    visit_stmts(stmt.body)

        visit_stmts(ast.main_body)
        for proc in ast.procedures:
            visit_stmts(proc.body)

        metrics.cyclomatic_complexity = complexity
        if complexity > 20:
            metrics.maintainability_rating = "C"
        elif complexity > 10:
            metrics.maintainability_rating = "B"

    # Generate Text Report
    lines = []
    lines.append("Summarization/Analysis Report")
    lines.append(f"Program: {path}")
    lines.append(f"Type: {'Free-Form' if ast and ast.is_free_format else 'Fixed-Format'} RPGLE")
    lines.append("I. Overview")
    lines.append(f"Total Lines: {len(source.splitlines())}")
    lines.append(f"Logical LOC: {metrics.sql_statement_count + metrics.variable_count + len(ast.main_body) if ast else 0}")
    lines.append(f"Procedural Complexity: {'Low' if metrics.cyclomatic_complexity < 5 else 'Medium'} ({metrics.cyclomatic_complexity})")
    lines.append(f"Database Access: {metrics.sql_statement_count} SQL Statements")
    lines.append(f"Type of Operations: Assignment, Call, SQL, Control Flow")
    lines.append("II. Metrics & Violations")
    lines.append(f"Maintainability Index: {metrics.maintainability_rating}")
    lines.append(f"Cyclomatic Complexity: {metrics.cyclomatic_complexity}")
    lines.append(f"Issues: {len(diagnostics)}")
    lines.append("III. Data Flow & Dependencies")
    lines.append(f"Files Used: (Derived from SQL/F-specs)")
    lines.append(f"Internal Variables: {metrics.variable_count} defined")
    
    report_text = "\n".join(lines)

    return RpgResult(
        path=path,
        ast=ast,
        diagnostics=diagnostics,
        metrics=metrics,
        summary_report=report_text,
        mermaid_diagram="\n".join(mermaid_lines),
        ast_tree="\n".join(ast_lines),
    )


if __name__ == "__main__":
    import sys

    path = sys.argv[1] if len(sys.argv) > 1 else "examples/example.rpgle"
    result = run_rpg_file(path)
    print(f"RPG Result: {result.path}")
    print(f"Diagnostics: {len(result.diagnostics)}")
    for d in result.diagnostics:
        print(f"  {d}")
    if result.summary_report:
        print(result.summary_report)
