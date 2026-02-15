"""
AST builder for DSPF DDS display files.

Walks parse tree from Speedy ANTLR/ANTLR4 and builds DisplayFile AST.
Fallback: line-based parser when ANTLR grammar not available.

DDS structure: A=attributes, R=record format. Col 1: spec type.
"""

import re
from core.diagnostics import Diagnostic
from dspf.ast_nodes import (
    DisplayFile,
    RecordFormat,
    Field,
    Attribute,
    SourceLocation,
)

FILENAME = "<memory>"


def parse_dspf(source: str, filename: str = FILENAME) -> tuple[DisplayFile, list[Diagnostic]]:
    """
    Parse DSPF DDS source into DisplayFile AST.

    Returns (ast, diagnostics).
    """
    diagnostics: list[Diagnostic] = []
    return _fallback_parse_dspf(source, filename, diagnostics)


def _fallback_parse_dspf(
    source: str, filename: str, diagnostics: list[Diagnostic]
) -> tuple[DisplayFile, list[Diagnostic]]:
    """Line-based fallback parser for DSPF DDS."""
    loc = SourceLocation(filename, 1, 0)
    record_formats: list[RecordFormat] = []
    current_record: RecordFormat | None = None
    file_keywords: dict[str, str] = {}

    lines = source.splitlines()
    for i, line in enumerate(lines):
        ln = i + 1
        stripped = line.strip()
        if not stripped or stripped.startswith("/*") or stripped[0] == "*":
            continue

        # Col 1: A (attributes/field) or R (record)
        spec = stripped[0].upper() if stripped else ""
        content = stripped[1:].strip() if len(stripped) > 1 else ""

        if spec == "R":
            # Record format: R RECORDNAME
            parts = content.split()
            name = parts[0] if parts else "unknown"
            current_record = RecordFormat(
                loc=SourceLocation(filename, ln, 0),
                name=name,
                keywords={},
            )
            record_formats.append(current_record)
        elif spec == "A" and current_record:
            # Field: A name, row, col, length, or attributes
            field = _parse_field_line(content, filename, ln)
            if field:
                current_record.fields.append(field)

    return DisplayFile(
        loc=loc,
        record_formats=record_formats,
        file_level_keywords=file_keywords,
    ), diagnostics


def _parse_field_line(content: str, filename: str, line: int) -> Field | None:
    """Parse an A-spec field line."""
    loc = SourceLocation(filename, line, 0)
    # DSPF A-spec: name, position, length, type, attributes
    # Simplified: first token = name, rest = pos/length/attrs
    parts = content.split()
    if not parts:
        return None
    name = parts[0]
    attrs: list[Attribute] = []
    keywords: dict[str, str] = {}
    row, col, length = None, None, None

    i = 1
    while i < len(parts):
        p = parts[i].upper()
        if p in ("DSPATR", "COLOR", "HI", "TEXT", "REF", "CHECK", "CHKMSGID"):
            attr_name = p
            attr_val = parts[i + 1] if i + 1 < len(parts) else None
            if attr_name == "REF" and attr_val:
                keywords["REF"] = attr_val
            else:
                attrs.append(Attribute(loc=loc, name=attr_name, value=attr_val))
            i += 2
        elif p.isdigit():
            nums = [int(p)]
            j = i + 1
            while j < len(parts) and parts[j].isdigit():
                nums.append(int(parts[j]))
                j += 1
            if len(nums) >= 1:
                row = nums[0]
            if len(nums) >= 2:
                col = nums[1]
            if len(nums) >= 3:
                length = nums[2]
            i = j
        else:
            i += 1

    return Field(
        loc=loc,
        name=name,
        row=row,
        col=col,
        length=length,
        attributes=attrs,
        keywords=keywords,
    )
