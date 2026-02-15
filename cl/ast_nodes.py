"""
Pythonic AST for CL/CLLE control language.

CL commands follow IBM i structure: command name, positional/keyword params,
expressions. Line-based; continuation via '+' at column 15.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class SourceLocation:
    """Location info for every AST node."""

    file: str
    line: int
    column: int = 0


@dataclass
class ClExpression:
    """Expression in a CL parameter (literal, variable, concatenation, etc.)."""

    loc: SourceLocation
    text: str
    children: list["ClExpression"] = field(default_factory=list)


@dataclass
class ClParameter:
    """Single parameter in a CL command (keyword or positional)."""

    loc: SourceLocation
    keyword: str | None  # e.g. "KWD" or None for positional
    value: ClExpression


@dataclass
class ClCommand:
    """Single CL command (e.g. CALL, DCL, IF)."""

    loc: SourceLocation
    name: str
    parameters: list[ClParameter] = field(default_factory=list)


@dataclass
class ClProgram:
    """Root AST node for a CL/CLLE program."""

    loc: SourceLocation
    name: str | None = None
    commands: list[ClCommand] = field(default_factory=list)
