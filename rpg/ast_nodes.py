"""
Pythonic AST for RPG / RPGLE / SQLRPGLE.

Supports both fixed-format (positional columns) and free-format.
Same AST node types for both; fixed vs free only affects parsing.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


@dataclass
class SourceLocation:
    """Location info for every AST node."""

    file: str
    line: int
    column: int = 0


@dataclass
class RpgExpr:
    """Expression node (literal, identifier, binary op, etc.)."""

    loc: SourceLocation
    kind: str  # "literal" | "ident" | "binary" | "call" | "sql" | ...
    value: str | None = None
    children: list["RpgExpr"] = field(default_factory=list)


@dataclass
class RpgParam:
    """Procedure/function parameter."""

    loc: SourceLocation
    name: str
    passing: str | None = None  # VALUE, CONST, etc.


@dataclass
class RpgVarDecl:
    """Variable declaration (D-spec)."""

    loc: SourceLocation
    name: str
    data_type: str | None = None
    length: str | None = None
    decimals: str | None = None
    inz: str | None = None


@dataclass
class EmbeddedSqlStmt:
    """Embedded SQL statement (EXEC SQL ... END-EXEC)."""

    loc: SourceLocation
    sql_text: str
    stmt_type: str | None = None  # SELECT, INSERT, UPDATE, DELETE, etc.


# Statement variants
@dataclass
class RpgAssignStmt:
    """Assignment statement."""

    loc: SourceLocation
    target: RpgExpr
    expr: RpgExpr


@dataclass
class RpgCallStmt:
    """Procedure/program call."""

    loc: SourceLocation
    name: str
    params: list[RpgExpr] = field(default_factory=list)


@dataclass
class RpgIfStmt:
    """IF/ELSEIF/ELSE/ENDIF."""

    loc: SourceLocation
    condition: RpgExpr
    then_body: list["RpgStatement"]
    else_if_parts: list[tuple[RpgExpr, list["RpgStatement"]]] = field(default_factory=list)
    else_body: list["RpgStatement"] = field(default_factory=list)


@dataclass
class RpgSelectStmt:
    """SELECT/WHEN/OTHER/ENDSL."""

    loc: SourceLocation
    cases: list[tuple[RpgExpr | None, list["RpgStatement"]]]  # None = OTHER


@dataclass
class RpgDoForStmt:
    """DO/DOU/DOU/FOR loop."""

    loc: SourceLocation
    kind: str  # "do" | "dou" | "dow" | "for"
    condition: RpgExpr | None = None
    body: list["RpgStatement"] = field(default_factory=list)


@dataclass
class RpgReturnStmt:
    """Return statement."""

    loc: SourceLocation
    value: RpgExpr | None = None


RpgStatement = (
    RpgAssignStmt
    | RpgCallStmt
    | RpgIfStmt
    | RpgSelectStmt
    | RpgDoForStmt
    | RpgReturnStmt
    | EmbeddedSqlStmt
)


@dataclass
class RpgProcedure:
    """Procedure (P-spec) or subprocedure."""

    loc: SourceLocation
    name: str
    params: list[RpgParam] = field(default_factory=list)
    body: list[RpgStatement] = field(default_factory=list)
    returns: str | None = None


@dataclass
class RpgProgram:
    """Root AST node for RPG/RPGLE/SQLRPGLE program."""

    loc: SourceLocation
    is_free_format: bool = True
    procedures: list[RpgProcedure] = field(default_factory=list)
    main_body: list[RpgStatement] = field(default_factory=list)
    variables: list[RpgVarDecl] = field(default_factory=list)
    sql_statements: list[EmbeddedSqlStmt] = field(default_factory=list)
