"""
Pipeline configuration and mode selection.

Modes:
- auto: Infer artifact kind from extension / content sniffing.
- cl, rpg, db2, dspf: Run only that module.
- combined: Run all applicable modules on given inputs.
"""

from dataclasses import dataclass
from pathlib import Path

# Extension -> kind mapping for auto inference.
EXT_TO_KIND: dict[str, str] = {
    ".cl": "cl",
    ".clle": "cl",
    ".rpg": "rpg",
    ".rpgle": "rpg",
    ".sql": "db2",
    ".dspf": "dspf",
}


def infer_kind_from_path(path: str | Path) -> str:
    """
    Infer artifact kind from file path (extension).

    Returns: "cl" | "rpg" | "db2" | "dspf" | "auto"
    """
    ext = Path(path).suffix.lower()
    return EXT_TO_KIND.get(ext, "auto")


def infer_kind_from_content(content: str, filename: str = "") -> str:
    """
    Quick content sniff to infer kind when extension is ambiguous.

    Heuristics:
    - CL: PGM, DCL, CALL, SBMJOB, etc. at start of line
    - RPG: **FREE, F-spec, D-spec, C-spec indicators
    - DB2: SELECT, INSERT, CREATE TABLE, etc.
    - DSPF: A, R, and record format / field keywords
    """
    line = content.split("\n")[0].strip()[:80].upper()
    if line.startswith("**FREE") or "FMT" in line[:6] or line[:7].strip() in ("D", "C", "F", "P"):
        return "rpg"
    if any(
        kw in line
        for kw in ("SELECT ", "INSERT ", "UPDATE ", "DELETE ", "CREATE TABLE", "CREATE VIEW")
    ):
        return "db2"
    if any(kw in line for kw in ("PGM", "DCL", "CALL ", "SBMJOB", "RUNSQL ")):
        return "cl"
    if line.startswith("A ") or line.startswith("R ") or "RECORD" in line[:20]:
        return "dspf"
    return infer_kind_from_path(filename) if filename else "auto"
