"""
File loading helpers for IBM i source artifacts.

Supports reading CL, RPG, DB2, and DSPF source files with encoding handling
(common IBM i encodings: EBCDIC, UTF-8, Latin-1).
"""

from pathlib import Path


# Common IBM i encodings; try in order when loading files.
DEFAULT_ENCODINGS = ("utf-8", "cp037", "cp500", "latin-1")


def load_file(path: str | Path, encodings: tuple[str, ...] | None = None) -> str:
    """
    Load a source file with fallback encodings.

    Args:
        path: Path to the source file.
        encodings: Tuple of encodings to try (default: utf-8, cp037, cp500, latin-1).

    Returns:
        File contents as string.

    Raises:
        FileNotFoundError: If the file does not exist.
        UnicodeDecodeError: If none of the encodings succeed.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(str(path))

    encodings = encodings or DEFAULT_ENCODINGS
    last_err: BaseException | None = None

    for enc in encodings:
        try:
            return path.read_text(encoding=enc)
        except UnicodeDecodeError as e:
            last_err = e

    if last_err:
        raise last_err
    raise UnicodeDecodeError("unknown", b"", 0, 1, "no encoding succeeded")


def discover_files(
    root: str | Path,
    include_patterns: list[str] | None = None,
    exclude_patterns: list[str] | None = None,
) -> list[Path]:
    """
    Discover source files under a project root directory.

    Args:
        root: Root directory to search.
        include_patterns: Glob patterns (e.g. *.rpgle, *.clle). Default: all known extensions.
        exclude_patterns: Glob patterns to exclude (e.g. *bak*, *old*).

    Returns:
        Sorted list of matching file paths.
    """
    root = Path(root)
    if not root.is_dir():
        return []

    default_includes = ["*.cl", "*.clle", "*.rpg", "*.rpgle", "*.sql", "*.dspf"]
    patterns = include_patterns or default_includes

    seen: set[Path] = set()
    for pat in patterns:
        seen.update(root.rglob(pat))

    exclude_patterns = exclude_patterns or []
    for pat in exclude_patterns:
        to_remove = [p for p in seen if Path(pat).match(str(p)) or pat in str(p)]
        for p in to_remove:
            seen.discard(p)

    return sorted(seen)
