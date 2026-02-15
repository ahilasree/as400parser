"""
Generate Python lexer/parser from ANTLR grammars.

Requires: Java JRE and ANTLR 4 jar, or antlr4-tool (pip install antlr4-tool).

Usage: python scripts/generate_parsers.py
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GRAMMARS = ROOT / "grammars"

# Grammar pairs: (lexer_g4, parser_g4, output_dir)
# Order: lexer first, then parser (parser depends on lexer tokens)
# Note: sqlrpgle and dspf grammars have syntax issues; CL and DB2 work.
CONFIGS = [
    ("clle_lexer.g4", "clle_parser.g4", ROOT / "cl" / "gen"),
    ("db2_lexer.g4", "db2_parser.g4", ROOT / "db2" / "gen"),
    # ("sqlrpgle_lexer.g4", "sqlrpgle_parser.g4", ROOT / "rpg" / "gen"),  # grammar name mismatch, syntax errors
    # ("dspf_lexer.g4", "dspf_parser.g4", ROOT / "dspf" / "gen"),  # syntax errors in grammar
]


def find_antlr_jar() -> Path | None:
    """Find ANTLR jar in antlr4-tool site-packages."""
    try:
        import antlr4
        pkg = Path(antlr4.__file__).parent
        # antlr4-tool puts jar in antlr4/bin or nearby
        for loc in [pkg / "bin", pkg.parent / "antlr4" / "bin", pkg.parent]:
            for f in loc.glob("antlr*.jar") if loc.exists() else []:
                return f
    except ImportError:
        pass
    return None


def run_antlr4(grammar_path: Path, output_dir: Path) -> bool:
    """Run ANTLR4 to generate Python parser. Returns True on success."""
    output_dir.mkdir(parents=True, exist_ok=True)
    cmd = [
        "java", "-jar", str(ANTLR_JAR),
        "-Dlanguage=Python3",
        "-visitor",
        "-no-listener",
        "-o", str(output_dir),
        str(grammar_path),
    ]
    try:
        r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=60)
        if r.returncode != 0:
            print(f"ANTLR error for {grammar_path.name}: {r.stderr}")
            return False
        return True
    except subprocess.TimeoutExpired:
        print(f"Timeout generating {grammar_path.name}")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def main() -> int:
    global ANTLR_JAR

    # Try antlr4 command first (from antlr4-tool)
    antlr_cmd = shutil.which("antlr4")
    if antlr_cmd:
        print("Using antlr4 command:", antlr_cmd)
        for lex_g4, par_g4, out_dir in CONFIGS:
            lex_path = GRAMMARS / lex_g4
            par_path = GRAMMARS / par_g4
            if not lex_path.exists() or not par_path.exists():
                print(f"Skip: {lex_g4}/{par_g4} not found")
                continue
            out_dir.mkdir(parents=True, exist_ok=True)
            for g in [lex_path, par_path]:
                cmd = [antlr_cmd, "-Dlanguage=Python3", "-visitor", "-o", str(out_dir), str(g)]
                r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
                if r.returncode != 0:
                    print(f"Failed {g.name}: {r.stderr}")
                else:
                    print(f"Generated from {g.name} -> {out_dir}")
        _write_gen_init()
        return 0

    # Fallback: use Java + jar
    ANTLR_JAR = find_antlr_jar()
    if not ANTLR_JAR or not ANTLR_JAR.exists():
        # Try common locations
        for p in [ROOT / "antlr-4.13.1-complete.jar", ROOT / "antlr4.jar"]:
            if p.exists():
                ANTLR_JAR = p
                break
    if not ANTLR_JAR or not ANTLR_JAR.exists():
        print("ANTLR not found. Install with:")
        print("  pip install antlr4-tool")
        print("Or download antlr-4.13.1-complete.jar and place in project root.")
        return 1

    print("Using ANTLR jar:", ANTLR_JAR)
    ok = True
    for lex_g4, par_g4, out_dir in CONFIGS:
        for g4 in [lex_g4, par_g4]:
            p = GRAMMARS / g4
            if p.exists():
                if run_antlr4(p, out_dir):
                    print(f"Generated {g4} -> {out_dir}")
                else:
                    ok = False
            else:
                print(f"Skip: {g4} not found")
    _write_gen_init()
    return 0 if ok else 1


def _write_gen_init():
    """Write __init__.py in each gen dir so they are importable."""
    for _, _, out_dir in CONFIGS:
        init = out_dir / "__init__.py"
        if out_dir.exists() and not init.exists():
            init.write_text("# Generated parser package\n")


if __name__ == "__main__":
    sys.exit(main())
