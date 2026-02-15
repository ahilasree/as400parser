# IBM i Artifact Parser

Modular Python codebase for parsing and analyzing IBM i artifacts (CL, RPG, DB2, DSPF).

## Requirements

- Python 3.11+
- Dependencies in `requirements.txt` (ANTLR4 runtime, reportlab for PDF export)

## Quick Start

```bash
# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1    # Windows PowerShell
# source venv/bin/activate     # Linux/macOS

# Install dependencies
pip install -r requirements.txt

# Run examples
python run_examples.py

# Run pipeline on example files
python main.py --mode combined examples/example.clle examples/example.rpgle examples/schema.sql examples/display.dspf
```

## Project Structure

```
AS400Parser/
├── core/               # Shared utilities
│   ├── diagnostics.py  # Error/warning model
│   ├── io.py           # File loading helpers
│   ├── config.py       # Pipeline configuration
│   ├── antlr_listener.py  # ANTLR error listener
│   ├── export_pdf.py   # Optional PDF export
│   └── emailer.py      # Optional email sending
├── cl/                 # CL/CLLE module
│   ├── gen/            # Generated lexer/parser (from grammars)
│   ├── ast_nodes.py
│   ├── ast_builder.py
│   └── runner.py
├── rpg/                # RPG/RPGLE/SQLRPGLE module
│   ├── ast_nodes.py
│   ├── ast_builder.py
│   └── runner.py
├── db2/                # DB2 SQL module
│   ├── gen/            # Generated lexer/parser (from grammars)
│   ├── ast_nodes.py
│   ├── ast_builder.py
│   └── runner.py
├── dspf/               # DSPF DDS module
│   ├── ast_nodes.py
│   ├── ast_builder.py
│   └── runner.py
├── ui/                 # Tkinter UI
│   └── main_ui.py
├── grammars/           # ANTLR grammar files (.g4)
├── scripts/            # Build/generation scripts
│   └── generate_parsers.py
├── examples/           # Example snippets
├── main.py             # Central dispatcher
├── run_examples.py     # Example usage
├── requirements.txt    # Dependencies
├── pyproject.toml      # Project metadata
├── .gitignore
├── DIAGRAMS.md         # Mermaid diagrams
└── README.md
```

## Usage

### CLI

```bash
python main.py --mode combined examples/example.clle examples/example.rpgle examples/schema.sql examples/display.dspf
```

With PDF export:

```bash
python main.py --mode combined --export-pdf output/report.pdf examples/example.clle examples/example.rpgle
```

With email report (requires SMTP config):

```bash
python main.py --mode combined --export-pdf output/report.pdf --email-to user@example.com --smtp-host smtp.example.com --smtp-port 587 --smtp-user user --smtp-pass pass --smtp-tls examples/*.clle examples/*.rpgle
```

### Programmatic

```python
from main import run_pipeline, InputSpec

inputs = [
    InputSpec(path="prog.clle", kind="cl"),
    InputSpec(path="prog.rpgle", kind="rpg"),
]
result = run_pipeline(inputs, mode="combined")
print(result.diagnostics)
```

### Per-language runners

```python
from cl.runner import run_cl_file
from rpg.runner import run_rpg_file
from db2.runner import run_db2_file
from dspf.runner import run_dspf_file

cl_result = run_cl_file("prog.clle")
rpg_result = run_rpg_file("prog.rpgle")
```

### UI

Launch the Tkinter UI to select files/folders, configure mode and output, and run analysis:

```bash
python -m ui.main_ui
```

## Pipeline Modes

- `auto` – Infer artifact kind from file extension and content
- `cl` – Parse only CL/CLLE files
- `rpg` – Parse only RPG/RPGLE/SQLRPGLE files
- `db2` – Parse only DB2 SQL files
- `dspf` – Parse only DSPF DDS files
- `combined` – Parse all applicable artifact types (default)

## ANTLR Grammar Integration

Grammars are in `grammars/`. Generate Python lexer/parser with:

```bash
# Install antlr4-tools (includes ANTLR jar)
pip install antlr4-tools

# Generate parsers for CL and DB2 (RPG and DSPF grammars have syntax issues)
python scripts/generate_parsers.py
```

CL and DB2 modules use the generated parsers from `cl/gen/` and `db2/gen/` when available; they fall back to line-based/statement-splitting parsers otherwise. RPG and DSPF use fallback parsers until their grammars are fixed.

## Diagrams

See `DIAGRAMS.md` for Mermaid diagram code blocks visualizing the architecture and workflows.

## Troubleshooting

- **ImportError: cannot import name 'dataclass'** – Ensure there is no file named `ast.py` in the project root, as it shadows Python’s built-in `ast` module. If you have a custom AST module, rename it (e.g. to `legacy_ast.py`).
