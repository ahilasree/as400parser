"""
Shared error/warning diagnostic model for all IBM i artifact parsers.

All parse modules report issues through Diagnostic instances, which are
aggregated in PipelineResult and per-module *Result types.
"""

from dataclasses import dataclass, field


@dataclass
class Diagnostic:
    """Single diagnostic (error or warning) from parsing or analysis."""

    file: str
    line: int
    column: int
    severity: str  # "error" | "warning"
    message: str

    def __str__(self) -> str:
        return f"{self.file}:{self.line}:{self.column}: [{self.severity}] {self.message}"


@dataclass
class ParseError(Exception):
    """Raised when parsing fails; carries the list of diagnostics."""

    errors: list["Diagnostic"] = field(default_factory=list)

    def __init__(self, errors: list[Diagnostic]):
        self.errors = errors
        super().__init__("Parse failed: " + "; ".join(str(e) for e in errors[:3]))


def is_error(d: Diagnostic) -> bool:
    """Check if diagnostic is an error."""
    return d.severity == "error"


def is_warning(d: Diagnostic) -> bool:
    """Check if diagnostic is a warning."""
    return d.severity == "warning"
