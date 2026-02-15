from dataclasses import dataclass
from typing import List
from antlr4.error.ErrorListener import ErrorListener

@dataclass
class Diagnostic:
    file: str
    line: int
    column: int
    severity: str  # "error" | "warning"
    message: str

class CollectingErrorListener(ErrorListener):
    """
    Shared ANTLR error listener that collects diagnostics.
    """
    def __init__(self, filename: str):
        self.filename = filename
        self.diagnostics: List[Diagnostic] = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.diagnostics.append(Diagnostic(self.filename, line, column, "error", msg))