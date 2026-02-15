"""
AST builder for CL/CLLE.

Uses generated ANTLR parser (cl.gen) when available; falls back to line-based
parser when grammars are not generated. Same AST structure in both cases.
"""

import re
from core.diagnostics import Diagnostic
from core.antlr_listener import HAS_ANTLR, DiagnosticErrorListener
from cl.ast_nodes import (
    ClProgram,
    ClCommand,
    ClParameter,
    ClExpression,
    SourceLocation,
)

FILENAME = "<memory>"

try:
    from cl.gen.clle_parserVisitor import clle_parserVisitor
except ImportError:
    clle_parserVisitor = None  # type: ignore


def parse_cl(source: str, filename: str = FILENAME) -> tuple[ClProgram, list[Diagnostic]]:
    """
    Parse CL/CLLE source into ClProgram AST.

    Uses ANTLR parser from cl.gen when available; otherwise line-based fallback.
    IBM i note: CL lines are 100 cols; col 6 for continuation, 16+ for command/params.
    """
    diagnostics: list[Diagnostic] = []

    try:
        ast = _parse_with_antlr(source, filename, diagnostics)
        if ast is not None:
            return ast, diagnostics
    except ImportError:
        pass

    return _fallback_parse_cl(source, filename, diagnostics), diagnostics


def _parse_with_antlr(source: str, filename: str, diagnostics: list[Diagnostic]) -> ClProgram | None:
    """Parse using generated clle_lexer/clle_parser. Returns None on parse error."""
    if not HAS_ANTLR:
        return None
    try:
        from antlr4 import InputStream, CommonTokenStream
        from cl.gen.clle_lexer import clle_lexer
        from cl.gen.clle_parser import clle_parser
        from cl.gen.clle_parserVisitor import clle_parserVisitor
    except ImportError:
        return None

    stream = InputStream(source)
    lexer = clle_lexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = clle_parser(tokens)

    err_listener = DiagnosticErrorListener(filename=filename, diagnostics=diagnostics)
    parser.removeErrorListeners()
    parser.addErrorListener(err_listener)

    try:
        tree = parser.program()
    except Exception:
        return None

    if diagnostics and any(d.severity == "error" for d in diagnostics):
        return None

    if ClAstVisitor is None:
        return None

    visitor = ClAstVisitor(filename)
    return visitor.visit(tree)


if clle_parserVisitor is not None:

    class ClAstVisitor(clle_parserVisitor):
        """Builds ClProgram AST from clle_parser parse tree."""

        def __init__(self, filename: str):
            self.filename = filename
            self._commands: list[ClCommand] = []

        def visitProgram(self, ctx):
            self._commands = []
            for stmt in ctx.statement():
                self.visit(stmt)
            loc = SourceLocation(self.filename, ctx.start.line if ctx.start else 1, ctx.start.column if ctx.start else 0)
            return ClProgram(loc=loc, commands=self._commands)

        def visitStatement(self, ctx):
            if ctx.command():
                cmd_ctx = ctx.command()
                name = cmd_ctx.COMMAND().getText() if cmd_ctx.COMMAND() else ""
                params: list[ClParameter] = []
                for i in range(len(cmd_ctx.PARAMETER())):
                    param_tok = cmd_ctx.PARAMETER(i)
                    ptext = param_tok.getText()
                    line = param_tok.line if param_tok else 1
                    loc = SourceLocation(self.filename, line, param_tok.column if param_tok else 0)
                    if "=" in ptext:
                        kw, _, val = ptext.split("=", 1)
                        params.append(ClParameter(loc=loc, keyword=kw.strip().upper() or None,
                                                  value=ClExpression(loc, val.strip())))
                    else:
                        params.append(ClParameter(loc=loc, keyword=None, value=ClExpression(loc, ptext)))
                cmd_loc = SourceLocation(self.filename, cmd_ctx.start.line if cmd_ctx.start else 1,
                                         cmd_ctx.start.column if cmd_ctx.start else 0)
                self._commands.append(ClCommand(loc=cmd_loc, name=name.upper(), parameters=params))
            else:
                return self.visitChildren(ctx)
            return None

else:
    ClAstVisitor = None  # type: ignore


def _fallback_parse_cl(source: str, filename: str, diagnostics: list[Diagnostic]) -> ClProgram:
    """Line-based fallback parser when ANTLR grammar not generated."""
    lines = source.splitlines()
    commands: list[ClCommand] = []
    loc = SourceLocation(file=filename, line=1, column=0)

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.rstrip()
        if not stripped or stripped.startswith("/*") or stripped[0] == "*":
            i += 1
            continue

        cmd_lines = [line]
        j = i + 1
        while j < len(lines) and len(lines[j]) >= 6 and lines[j][5:6].strip() == "+":
            cmd_lines.append(lines[j])
            j += 1

        full_cmd = " ".join(
            ln[15:].rstrip() if len(ln) > 15 else ln
            for ln in cmd_lines
        ).strip()

        if full_cmd:
            cmd = _parse_command_line(full_cmd, filename, i + 1, diagnostics)
            if cmd:
                commands.append(cmd)
        i = j

    return ClProgram(loc=loc, commands=commands)


def _parse_command_line(text: str, filename: str, line: int, diagnostics: list[Diagnostic]) -> ClCommand | None:
    parts = _split_cl_params(text)
    if not parts:
        return None

    name = parts[0].upper()
    params: list[ClParameter] = []
    for p in parts[1:]:
        if "=" in p:
            kw, _, val = p.split("=", 1)
            params.append(ClParameter(
                loc=SourceLocation(filename, line, 0),
                keyword=kw.strip().upper() or None,
                value=ClExpression(SourceLocation(filename, line, 0), val.strip()),
            ))
        else:
            params.append(ClParameter(
                loc=SourceLocation(filename, line, 0),
                keyword=None,
                value=ClExpression(SourceLocation(filename, line, 0), p),
            ))
    return ClCommand(loc=SourceLocation(filename, line, 0), name=name, parameters=params)


def _split_cl_params(text: str) -> list[str]:
    result: list[str] = []
    current: list[str] = []
    in_quote = False
    quote_char = ""
    i = 0
    while i < len(text):
        c = text[i]
        if not in_quote:
            if c in ("'", '"'):
                in_quote = True
                quote_char = c
                current.append(c)
            elif c.isspace():
                if current:
                    result.append("".join(current))
                    current = []
            else:
                current.append(c)
        else:
            current.append(c)
            if c == quote_char:
                in_quote = False
        i += 1
    if current:
        result.append("".join(current))
    return result
