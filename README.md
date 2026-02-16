# IBM i Artifact Parser

Modular Python codebase for parsing and analyzing IBM i artifacts (CL, RPG, DB2, DSPF).

## Requirements

- Python 3.11+
- Docker (for containerization)
- kubectl (for Kubernetes deployment)
- Google Cloud SDK (for GCP deployment)

### Dependencies

Install all required packages:

```bash
# Core dependencies
antlr4-python3-runtime>=4.13.0
antlr4-tools>=0.2.2
reportlab>=4.0.0

# Web API
flask>=3.1.0
flask-cors>=4.0.0
waitress>=3.0.0

# Email and utilities
smtplib-ssl>=1.0.0
python-dotenv>=1.0.0

# Production
gunicorn>=21.0.0

# Testing
pytest>=7.0.0
pytest-flask>=1.2.0
```

Install with:
```bash
pip install -r requirements.txt
```

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
├── api/                # Web API endpoint
│   └── app.py
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

### Web API

Start the REST API server:

```bash
# Development mode
python api/app.py

# Production mode
gunicorn --bind 0.0.0.0:5000 api.app:app
```

API endpoint: `http://localhost:5000/api/parse`

```bash
curl -X POST http://localhost:5000/api/parse \
  -H "Content-Type: application/json" \
  -d '{
    "files": ["examples/example.clle"],
    "mode": "combined",
    "enable_pdf": true,
    "enable_email": true,
    "email_config": {
      "to": "user@example.com",
      "smtp_host": "smtp.gmail.com",
      "smtp_user": "user@gmail.com",
      "smtp_pass": "password",
      "smtp_tls": "true"
    }
  }'
```

#### API Endpoints

- `GET /health` - Health check
- `GET /api/parse` - API documentation
- `POST /api/parse` - Parse IBM i files

#### API Response Format

```json
{
  "success": true,
  "diagnostics_count": 0,
  "cl_results": 1,
  "rpg_results": 0,
  "db2_results": 0,
  "dspf_results": 0,
  "analysis_reports": [
    {
      "file": "examples/example.clle",
      "type": "CL",
      "report": "Analysis report content...",
      "ast_tree": "ASCII tree representation..."
    }
  ]
}
```

## Docker Deployment

### Build Docker Image

```bash
# Build the image
docker build -t as400parser:latest .

# Run locally
docker run -p 5000:5000 as400parser:latest
```

### Docker Compose

```bash
# Start with docker-compose
docker-compose up -d

# Stop
docker-compose down
```

## Kubernetes Deployment on GCP

### Prerequisites

1. Install Google Cloud SDK
2. Install kubectl
3. Authenticate with GCP

```bash
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
gcloud container clusters get-credentials YOUR_CLUSTER_NAME --zone YOUR_ZONE
```

### Deploy to GKE

```bash
# Apply all configurations
kubectl apply -f k8s/

# Check deployment
kubectl get pods -n as400parser

# Get service URL
kubectl get service as400parser-service -n as400parser
```

### Kubernetes Components

- **Namespace**: `as400parser`
- **Deployment**: 3 replicas with resource limits
- **Service**: LoadBalancer type for external access
- **ConfigMap**: Environment configuration
- **Secret**: SMTP credentials (optional)

### Monitoring and Scaling

```bash
# Scale deployment
kubectl scale deployment as400parser --replicas=5 -n as400parser

# View logs
kubectl logs -f deployment/as400parser -n as400parser

# Monitor resources
kubectl top pods -n as400parser
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
python ui/main_ui.py
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

- **ImportError: cannot import name 'dataclass'** – Ensure there is no file named `ast.py` in the project root, as it shadows Python's built-in `ast` module. If you have a custom AST module, rename it (e.g. to `legacy_ast.py`).
