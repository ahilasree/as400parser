"""
Reusable ANTLR/Speedy error listener that produces Diagnostic instances.

Use this for all parse modules to get consistent error reporting.
"""

from dataclasses import dataclass

from core.diagnostics import Diagnostic

# ANTLR4 provides BaseErrorListener; we implement a custom one.
# Lazy import to allow running without antlr4 installed during development.
try:
    from antlr4 import Recognizer
    from antlr4.error.Errors import RecognitionException
    from antlr4.error.ErrorListener import ErrorListener as _ErrorListener
    HAS_ANTLR = True
except ImportError:
    HAS_ANTLR = False
    Recognizer = None  # type: ignore
    RecognitionException = None  # type: ignore
    _ErrorListener = object  # type: ignore


@dataclass
class DiagnosticErrorListener(_ErrorListener):
    """
    ANTLR error listener that collects syntax errors as Diagnostic instances.
    """

    filename: str = "<memory>"
    diagnostics: list[Diagnostic] = None

    def __post_init__(self):
        if self.diagnostics is None:
            self.diagnostics = []

    def syntaxError(
        self,
        recognizer: "Recognizer",
        offendingSymbol: object,
        line: int,
        charPositionInLine: int,
        msg: str,
        e: "RecognitionException | None" = None,
    ) -> None:
        self.diagnostics.append(
            Diagnostic(
                file=self.filename,
                line=line,
                column=charPositionInLine,
                severity="error",
                message=msg,
            )
        )
