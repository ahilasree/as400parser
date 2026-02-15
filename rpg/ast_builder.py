"""
AST builder for RPG / RPGLE / SQLRPGLE.

Walks parse tree from Speedy ANTLR/ANTLR4 and builds RpgProgram AST.
Fixed and free format map to same AST node types.
Fallback: line-based parser when ANTLR grammar not available.
"""

import re
from core.diagnostics import Diagnostic
from rpg.ast_nodes import (
    RpgProgram,
    RpgProcedure,
    RpgParam,
    RpgVarDecl,
    RpgExpr,
    RpgAssignStmt,
    RpgCallStmt,
    RpgReturnStmt,
    EmbeddedSqlStmt,
    SourceLocation,
)

FILENAME = "<memory>"


def parse_rpg(source: str, filename: str = FILENAME) -> tuple[RpgProgram, list[Diagnostic]]:
    """
    Parse RPG/RPGLE/SQLRPGLE source into RpgProgram AST.

    Detects fixed vs free format: **FREE in first line => free.
    Returns (ast, diagnostics).
    """
    diagnostics: list[Diagnostic] = []
    lines = source.splitlines()
    if not lines:
        return RpgProgram(loc=SourceLocation(filename, 0, 0)), diagnostics

    first = lines[0].strip()
    is_free = first.upper().startswith("**FREE") or first.upper().startswith("/FREE")

    if is_free:
        return _parse_rpg_free(source, filename, diagnostics)
    return _parse_rpg_fixed(source, filename, diagnostics)


def _parse_rpg_free(source: str, filename: str, diagnostics: list[Diagnostic]) -> tuple[RpgProgram, list[Diagnostic]]:
    """Parse free-format RPG."""
    loc = SourceLocation(filename, 1, 0)
    procedures: list[RpgProcedure] = []
    main_body: list = []
    variables: list[RpgVarDecl] = []
    sql_statements: list[EmbeddedSqlStmt] = []

    lines = source.splitlines()
    i = 0
    in_procedure = False
    current_proc: RpgProcedure | None = None
    proc_body: list = []

    while i < len(lines):
        line = lines[i]
        ln = i + 1
        # Skip **FREE, /FREE, /END-FREE
        s = line.strip()
        if s.upper() in ("**FREE", "/FREE", "/END-FREE") or not s or s.startswith("//"):
            i += 1
            continue

        # EXEC SQL ... END-EXEC
        if "EXEC SQL" in s.upper():
            sql_start = s.upper().find("EXEC SQL")
            sql_text = _extract_embedded_sql(lines[i:], sql_start)
            stmt_type = _guess_sql_type(sql_text)
            sql_statements.append(
                EmbeddedSqlStmt(
                    loc=SourceLocation(filename, ln, 0),
                    sql_text=sql_text,
                    stmt_type=stmt_type,
                )
            )
            i += sql_text.count("\n") + 1
            continue

        # Dcl-s (D-spec)
        if re.match(r"^dcl[- ]?[s ]", s.lower()) or re.match(r"^d\s+", s, re.I):
            # Simplified D-spec: Dcl-S name type;
            m = re.search(r"dcl[- ]?s\s+(\w+)\s+(\w+)", s, re.I)
            if m:
                variables.append(
                    RpgVarDecl(
                        loc=SourceLocation(filename, ln, 0),
                        name=m.group(1),
                        data_type=m.group(2),
                    )
                )
            i += 1
            continue

        # Dcl-Proc / End-Proc
        if "dcl-proc" in s.lower():
            m = re.search(r"dcl-proc\s+(\w+)", s, re.I)
            name = m.group(1) if m else "unknown"
            current_proc = RpgProcedure(loc=SourceLocation(filename, ln, 0), name=name)
            proc_body = []
            in_procedure = True
        elif "end-proc" in s.lower() and current_proc:
            current_proc.body = proc_body
            procedures.append(current_proc)
            current_proc = None
            in_procedure = False
        elif in_procedure and current_proc:
            stmt = _parse_free_stmt(s, filename, ln)
            if stmt:
                proc_body.append(stmt)
        else:
            stmt = _parse_free_stmt(s, filename, ln)
            if stmt:
                main_body.append(stmt)

        i += 1

    return (
        RpgProgram(
            loc=loc,
            is_free_format=True,
            procedures=procedures,
            main_body=main_body,
            variables=variables,
            sql_statements=sql_statements,
        ),
        diagnostics,
    )


def _parse_rpg_fixed(source: str, filename: str, diagnostics: list[Diagnostic]) -> tuple[RpgProgram, list[Diagnostic]]:
    """Parse fixed-format RPG. Spec type in col 6, content in 7-80."""
    loc = SourceLocation(filename, 1, 0)
    procedures: list[RpgProcedure] = []
    main_body: list = []
    variables: list[RpgVarDecl] = []
    sql_statements: list[EmbeddedSqlStmt] = []

    lines = source.splitlines()
    for i, line in enumerate(lines):
        ln = i + 1
        if len(line) < 7:
            continue
        spec = line[5:6].upper()  # col 6
        content = line[6:].rstrip() if len(line) > 6 else ""
        if not content.strip():
            continue

        if spec == "D":  # D-spec
            # D VARNAME     S              5  0
            parts = content.split()
            if len(parts) >= 2:
                name = parts[0]
                dt = parts[1] if len(parts) > 1 else None
                variables.append(
                    RpgVarDecl(loc=SourceLocation(filename, ln, 6), name=name, data_type=dt)
                )
        elif spec == "C":  # C-spec (calculation)
            # C                   EVAL      X = 1
            op = content[6:14].strip().upper() if len(content) > 14 else ""
            rest = content[14:].strip() if len(content) > 14 else content.strip()
            stmt = _parse_fixed_cspec(op, rest, filename, ln)
            if stmt:
                main_body.append(stmt)
        elif spec == "P":  # P-spec (procedure)
            name = content[:10].strip()
            procedures.append(
                RpgProcedure(loc=SourceLocation(filename, ln, 6), name=name or "unknown")
            )

    return (
        RpgProgram(
            loc=loc,
            is_free_format=False,
            procedures=procedures,
            main_body=main_body,
            variables=variables,
            sql_statements=sql_statements,
        ),
        diagnostics,
    )


def _extract_embedded_sql(lines: list[str], start_col: int) -> str:
    """Extract full embedded SQL from lines."""
    out: list[str] = []
    for line in lines:
        s = line.strip()
        out.append(s)
        if "END-EXEC" in s.upper() or "END-SQL" in s.upper():
            break
    return "\n".join(out)


def _guess_sql_type(sql: str) -> str | None:
    sql = sql.upper()
    for t in ("SELECT", "INSERT", "UPDATE", "DELETE", "DECLARE", "FETCH"):
        if t in sql and sql.index(t) < 50:
            return t
    return None


def _parse_free_stmt(s: str, filename: str, line: int) -> object | None:
    """Parse a single free-format statement line."""
    loc = SourceLocation(filename, line, 0)
    s = s.strip().rstrip(";")
    if not s:
        return None
    s_upper = s.upper()
    if s_upper.startswith("RETURN"):
        return RpgReturnStmt(loc=loc, value=None)
    if s_upper.startswith("CALL "):
        name = s[5:].split("(")[0].strip()
        return RpgCallStmt(loc=loc, name=name, params=[])
    if "=" in s and " EXEC " not in s_upper:
        idx = s.find("=")
        target = s[:idx].strip()
        expr = s[idx + 1 :].strip()
        return RpgAssignStmt(
            loc=loc,
            target=RpgExpr(loc=loc, kind="ident", value=target),
            expr=RpgExpr(loc=loc, kind="literal", value=expr),
        )
    return None


def _parse_fixed_cspec(op: str, rest: str, filename: str, line: int) -> object | None:
    """Parse fixed C-spec operation and rest."""
    loc = SourceLocation(filename, line, 6)
    op = op.upper()
    if op in ("EVAL", "EVALR", "EVAL-CORR"):
        if "=" in rest:
            t, _, e = rest.partition("=")
            return RpgAssignStmt(
                loc=loc,
                target=RpgExpr(loc=loc, kind="ident", value=t.strip()),
                expr=RpgExpr(loc=loc, kind="literal", value=e.strip()),
            )
    if op == "CALL":
        name = rest.split()[0] if rest else ""
        return RpgCallStmt(loc=loc, name=name, params=[])
    if op in ("RETURN", "LEAVE"):
        return RpgReturnStmt(loc=loc, value=None)
    return None
