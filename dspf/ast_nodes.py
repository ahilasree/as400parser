"""
Pythonic AST for DSPF (display file DDS).

Covers record formats (R), fields (A), and attributes (DSPATR, COLOR, etc.).
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
class Attribute:
    """Field attribute (DSPATR, COLOR, HI, etc.)."""

    loc: SourceLocation
    name: str  # DSPATR, COLOR, HI, etc.
    value: str | None = None


@dataclass
class Field:
    """Display file field (A-spec)."""

    loc: SourceLocation
    name: str
    row: int | None = None
    col: int | None = None
    length: int | None = None
    data_type: str | None = None
    attributes: list[Attribute] = field(default_factory=list)
    ref: str | None = None  # REF keyword reference
    keywords: dict[str, str] = field(default_factory=dict)


@dataclass
class RecordFormat:
    """Record format (R-spec) containing fields."""

    loc: SourceLocation
    name: str
    fields: list[Field] = field(default_factory=list)
    keywords: dict[str, str] = field(default_factory=dict)


@dataclass
class DisplayFile:
    """Root AST node for a DSPF DDS display file."""

    loc: SourceLocation
    name: str | None = None
    record_formats: list[RecordFormat] = field(default_factory=list)
    file_level_keywords: dict[str, str] = field(default_factory=dict)
