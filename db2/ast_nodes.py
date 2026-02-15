"""
Pythonic AST for DB2 SQL (standalone scripts and embedded SQL).

Covers SELECT, INSERT, UPDATE, DELETE, DDL (CREATE TABLE, etc.).
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
class TableRef:
    """Table reference (FROM/JOIN clause)."""

    loc: SourceLocation
    name: str
    alias: str | None = None
    schema: str | None = None


@dataclass
class ColumnRef:
    """Column reference."""

    loc: SourceLocation
    name: str
    table_alias: str | None = None
    schema: str | None = None


@dataclass
class Predicate:
    """Predicate/condition (WHERE, ON, HAVING)."""

    loc: SourceLocation
    kind: str  # "equals" | "and" | "or" | "in" | "like" | ...
    left: "Predicate | ColumnRef | None" = None
    right: "Predicate | ColumnRef | None | str" = None
    children: list["Predicate"] = field(default_factory=list)


@dataclass
class Db2Select:
    """SELECT statement."""

    loc: SourceLocation
    columns: list[ColumnRef | str] = field(default_factory=list)
    from_tables: list[TableRef] = field(default_factory=list)
    where: Predicate | None = None
    group_by: list[ColumnRef | str] = field(default_factory=list)
    order_by: list[tuple[ColumnRef | str, str]] = field(default_factory=list)  # col, ASC/DESC


@dataclass
class Db2Insert:
    """INSERT statement."""

    loc: SourceLocation
    table: TableRef
    columns: list[ColumnRef | str] = field(default_factory=list)
    values: list[str] | None = None
    select: Db2Select | None = None


@dataclass
class Db2Update:
    """UPDATE statement."""

    loc: SourceLocation
    table: TableRef
    set_clauses: list[tuple[ColumnRef | str, str]] = field(default_factory=list)  # col, value expr
    where: Predicate | None = None


@dataclass
class Db2Delete:
    """DELETE statement."""

    loc: SourceLocation
    table: TableRef
    where: Predicate | None = None


@dataclass
class Db2Ddl:
    """DDL statement (CREATE TABLE, CREATE VIEW, etc.)."""

    loc: SourceLocation
    kind: str  # "CREATE TABLE" | "CREATE VIEW" | "ALTER TABLE" | ...
    name: str
    schema: str | None = None
    body: str | None = None  # raw DDL text for complex cases


Db2Statement = Db2Select | Db2Insert | Db2Update | Db2Delete | Db2Ddl


@dataclass
class Db2Script:
    """Root AST node for a DB2 SQL script."""

    loc: SourceLocation
    statements: list[Db2Statement] = field(default_factory=list)
