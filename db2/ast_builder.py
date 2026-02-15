"""
AST builder for DB2 SQL.

Uses generated ANTLR parser (db2.gen) when available; falls back to
statement-splitting parser when grammars are not generated.
"""

import re
from core.diagnostics import Diagnostic
from core.antlr_listener import HAS_ANTLR, DiagnosticErrorListener
from db2.ast_nodes import (
    Db2Script,
    Db2Select,
    Db2Insert,
    Db2Update,
    Db2Delete,
    Db2Ddl,
    TableRef,
    ColumnRef,
    Predicate,
    SourceLocation,
)

FILENAME = "<memory>"

try:
    from db2.gen.db2_parserVisitor import db2_parserVisitor
except ImportError:
    db2_parserVisitor = None  # type: ignore


def parse_db2(source: str, filename: str = FILENAME) -> tuple[Db2Script, list[Diagnostic]]:
    """
    Parse DB2 SQL script into Db2Script AST.

    Uses ANTLR parser from db2.gen when available; otherwise statement-splitting fallback.
    """
    diagnostics: list[Diagnostic] = []

    try:
        ast = _parse_with_antlr(source, filename, diagnostics)
        if ast is not None:
            return ast, diagnostics
    except ImportError:
        pass

    return _fallback_parse_db2(source, filename, diagnostics)


def _parse_with_antlr(source: str, filename: str, diagnostics: list[Diagnostic]) -> Db2Script | None:
    """Parse using generated db2_lexer/db2_parser. Returns None on parse error."""
    if not HAS_ANTLR:
        return None
    try:
        from antlr4 import InputStream, CommonTokenStream
        from db2.gen.db2_lexer import db2_lexer
        from db2.gen.db2_parser import db2_parser
    except ImportError:
        return None

    stream = InputStream(source)
    lexer = db2_lexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = db2_parser(tokens)

    err_listener = DiagnosticErrorListener(filename=filename, diagnostics=diagnostics)
    parser.removeErrorListeners()
    parser.addErrorListener(err_listener)

    try:
        tree = parser.sqlScript()
    except Exception:
        return None

    if diagnostics and any(d.severity == "error" for d in diagnostics):
        return None

    if db2_parserVisitor is None:
        return None

    visitor = Db2AstVisitor(filename)
    return visitor.visit(tree)


if db2_parserVisitor is not None:

    class Db2AstVisitor(db2_parserVisitor):
        """Builds Db2Script AST from db2_parser parse tree."""

        def __init__(self, filename: str):
            self.filename = filename
            self._statements: list = []

        def visitSqlScript(self, ctx):
            self._statements = []
            for stmt_ctx in ctx.sqlStatement():
                result = self.visit(stmt_ctx)
                if result is not None:
                    self._statements.append(result)
            loc = SourceLocation(self.filename, ctx.start.line if ctx.start else 1, ctx.start.column if ctx.start else 0)
            return Db2Script(loc=loc, statements=self._statements)

        def visitSqlStatement(self, ctx):
            if ctx.selectStatement():
                return self.visit(ctx.selectStatement())
            if ctx.insertStatement():
                return self.visit(ctx.insertStatement())
            if ctx.updateStatement():
                return self.visit(ctx.updateStatement())
            if ctx.deleteStatement():
                return self.visit(ctx.deleteStatement())
            if ctx.createStatement():
                return self.visit(ctx.createStatement())
            return self.visitChildren(ctx)

        def visitSelectStatement(self, ctx):
            text = ctx.getText()
            loc = SourceLocation(self.filename, ctx.start.line if ctx.start else 1, ctx.start.column if ctx.start else 0)
            return _parse_select_from_text(text, self.filename, ctx.start.line if ctx.start else 1)

        def visitInsertStatement(self, ctx):
            text = ctx.getText()
            return _parse_insert_from_text(text, self.filename, ctx.start.line if ctx.start else 1)

        def visitUpdateStatement(self, ctx):
            text = ctx.getText()
            return _parse_update_from_text(text, self.filename, ctx.start.line if ctx.start else 1)

        def visitDeleteStatement(self, ctx):
            text = ctx.getText()
            return _parse_delete_from_text(text, self.filename, ctx.start.line if ctx.start else 1)

        def visitCreateStatement(self, ctx):
            text = ctx.getText()
            if "TABLE" in text.upper()[:20]:
                return _parse_create_table_from_text(text, self.filename, ctx.start.line if ctx.start else 1)
            if "VIEW" in text.upper()[:20]:
                return _parse_create_view_from_text(text, self.filename, ctx.start.line if ctx.start else 1)
            return None

else:
    Db2AstVisitor = None  # type: ignore


def _parse_select_from_text(text: str, filename: str, line: int) -> Db2Select:
    loc = SourceLocation(filename, line, 0)
    m = re.search(r"\bFROM\s+([\w.]+)(?:\s+(?:AS\s+)?(\w+))?", text, re.I | re.S)
    tables: list[TableRef] = []
    if m:
        tname = m.group(1)
        alias = m.group(2)
        schema = None
        if "." in tname:
            schema, tname = tname.split(".", 1)
        tables.append(TableRef(loc=loc, name=tname, alias=alias, schema=schema))
    cols: list = []
    if " FROM " in text.upper():
        cols_part = text[: text.upper().index(" FROM ")].strip()
        if cols_part.upper().startswith("SELECT"):
            cols_part = cols_part[6:].strip()
        if cols_part == "*":
            cols.append("*")
        else:
            for c in re.split(r",\s*", cols_part):
                cols.append(c.strip())
    return Db2Select(loc=loc, columns=cols, from_tables=tables)


def _parse_insert_from_text(text: str, filename: str, line: int) -> Db2Insert:
    loc = SourceLocation(filename, line, 0)
    m = re.search(r"\bINSERT\s+INTO\s+([\w.]+)", text, re.I)
    tname = m.group(1) if m else "unknown"
    schema = None
    if "." in tname:
        schema, tname = tname.split(".", 1)
    table = TableRef(loc=loc, name=tname, schema=schema)
    return Db2Insert(loc=loc, table=table)


def _parse_update_from_text(text: str, filename: str, line: int) -> Db2Update:
    loc = SourceLocation(filename, line, 0)
    m = re.search(r"\bUPDATE\s+([\w.]+)", text, re.I)
    tname = m.group(1) if m else "unknown"
    schema = None
    if "." in tname:
        schema, tname = tname.split(".", 1)
    table = TableRef(loc=loc, name=tname, schema=schema)
    return Db2Update(loc=loc, table=table)


def _parse_delete_from_text(text: str, filename: str, line: int) -> Db2Delete:
    loc = SourceLocation(filename, line, 0)
    m = re.search(r"\bDELETE\s+FROM\s+([\w.]+)", text, re.I)
    tname = m.group(1) if m else "unknown"
    schema = None
    if "." in tname:
        schema, tname = tname.split(".", 1)
    table = TableRef(loc=loc, name=tname, schema=schema)
    return Db2Delete(loc=loc, table=table)


def _parse_create_table_from_text(text: str, filename: str, line: int) -> Db2Ddl:
    loc = SourceLocation(filename, line, 0)
    m = re.search(r"\bCREATE\s+TABLE\s+([\w.]+)", text, re.I)
    name = m.group(1) if m else "unknown"
    schema = None
    if "." in name:
        schema, name = name.split(".", 1)
    return Db2Ddl(loc=loc, kind="CREATE TABLE", name=name, schema=schema, body=text)


def _parse_create_view_from_text(text: str, filename: str, line: int) -> Db2Ddl:
    loc = SourceLocation(filename, line, 0)
    m = re.search(r"\bCREATE\s+VIEW\s+([\w.]+)", text, re.I)
    name = m.group(1) if m else "unknown"
    schema = None
    if "." in name:
        schema, name = name.split(".", 1)
    return Db2Ddl(loc=loc, kind="CREATE VIEW", name=name, schema=schema, body=text)


def _fallback_parse_db2(
    source: str, filename: str, diagnostics: list[Diagnostic]
) -> tuple[Db2Script, list[Diagnostic]]:
    """Statement-splitting fallback parser for DB2 SQL."""
    loc = SourceLocation(filename, 1, 0)
    statements: list = []

    parts = re.split(r";\s*", source)
    line_num = 1
    for part in parts:
        part = part.strip()
        if not part or part.startswith("--"):
            continue
        stmt = _parse_statement(part.strip(), filename, line_num, diagnostics)
        if stmt:
            statements.append(stmt)
        line_num += part.count("\n") + 1

    return Db2Script(loc=loc, statements=statements), diagnostics


def _parse_statement(
    text: str, filename: str, line: int, diagnostics: list[Diagnostic]
):
    text_upper = text.upper().strip()
    if text_upper.startswith("SELECT"):
        return _parse_select_from_text(text, filename, line)
    if text_upper.startswith("INSERT"):
        return _parse_insert_from_text(text, filename, line)
    if text_upper.startswith("UPDATE"):
        return _parse_update_from_text(text, filename, line)
    if text_upper.startswith("DELETE"):
        return _parse_delete_from_text(text, filename, line)
    if text_upper.startswith("CREATE TABLE"):
        return _parse_create_table_from_text(text, filename, line)
    if text_upper.startswith("CREATE VIEW"):
        return _parse_create_view_from_text(text, filename, line)
    return None
