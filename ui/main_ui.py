"""
Minimal tkinter UI for IBM i artifact parser.

Allows selecting codebase path or files, mode, output folder, optional email,
and runs the pipeline with a responsive UI.
"""

import logging
import os
import sys
import threading
import tkinter as tk
from datetime import datetime
from pathlib import Path
from tkinter import filedialog, messagebox, ttk

# Ensure project root is on path
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# Try importing main to verify path setup
try:
    import main
except ImportError:
    # Fallback: append to path if insert didn't work as expected
    sys.path.append(str(ROOT))

from main import run_pipeline, InputSpec, ExportOptions

logger = logging.getLogger(__name__)


def load_email_config():
    """Load email configuration from .env.local file"""
    env_file = ROOT / ".env.local"
    config = {}
    
    try:
        if env_file.exists():
            with open(env_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#') and '=' in line:
                        try:
                            key, value = line.split('=', 1)
                            config[key] = value
                        except ValueError:
                            # Skip lines with malformed key=value format
                            continue
    except Exception as e:
        print(f"Warning: Could not load email config: {e}")
    
    return config


def main() -> None:
    """Entry point for the UI."""
    try:
        root = tk.Tk()
        root.title("IBM i Artifact Parser")
        root.geometry("700x600")
        root.minsize(500, 400)

        app = MainUI(root)
        app.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        root.mainloop()
    except KeyboardInterrupt:
        print("\nUI closed by user")
    except Exception as e:
        print(f"Error starting UI: {e}")
        messagebox.showerror("Error", f"Failed to start UI: {e}")


class MainUI(ttk.Frame):
    """Main UI frame."""

    def __init__(self, parent: tk.Tk, **kwargs):
        super().__init__(parent, **kwargs)

        self.input_mode = tk.StringVar(value="files")
        self.files: list[str] = []
        self.project_root = tk.StringVar(value="")
        self.include_patterns = tk.StringVar(value="*.rpgle,*.clle,*.sql,*.dspf")
        self.exclude_patterns = tk.StringVar(value="")
        self.mode = tk.StringVar(value="combined")
        self.output_folder = tk.StringVar(value=str(ROOT / "output"))
        self.enable_pdf = tk.BooleanVar(value=False)
        self.enable_email = tk.BooleanVar(value=False)
        self.email_to = tk.StringVar(value="")
        self.smtp_host = tk.StringVar(value="")
        self.smtp_port = tk.StringVar(value="587")
        self.smtp_user = tk.StringVar(value="")
        self.smtp_pass = tk.StringVar(value="")
        self.smtp_tls = tk.BooleanVar(value=True)

        # Auto-populate email settings from .env.local
        self._auto_populate_email_settings()

        self._build_ui()

    def _auto_populate_email_settings(self) -> None:
        """Auto-populate email settings from .env.local file (only when user enables email)"""
        config = load_email_config()
        
        if config:
            # Populate email fields if values exist, but don't auto-enable email
            if config.get('EMAIL_TO'):
                self.email_to.set(config['EMAIL_TO'])
                
            if config.get('SMTP_HOST'):
                self.smtp_host.set(config['SMTP_HOST'])
                
            if config.get('SMTP_PORT'):
                self.smtp_port.set(config['SMTP_PORT'])
                
            if config.get('SMTP_USER'):
                self.smtp_user.set(config['SMTP_USER'])
                
            if config.get('SMTP_PASS'):
                self.smtp_pass.set(config['SMTP_PASS'])
                
            if config.get('SMTP_TLS'):
                self.smtp_tls.set(config['SMTP_TLS'].lower() == 'true')
                
            # Only auto-enable PDF if email is configured (but not email itself)
            if config.get('EMAIL_TO') and config.get('SMTP_HOST'):
                self.enable_pdf.set(True)
                
            # Log the auto-population
            print(f"Email settings loaded (will activate when enabled): TO={config.get('EMAIL_TO', 'Not set')}, SMTP={config.get('SMTP_HOST', 'Not set')}")

    def _build_ui(self) -> None:
        row = 0

        # Input mode
        f = ttk.LabelFrame(self, text="Input", padding=5)
        f.grid(row=row, column=0, columnspan=2, sticky="ew", pady=2)
        ttk.Radiobutton(f, text="Single/Multiple files", variable=self.input_mode, value="files").pack(anchor="w")
        ttk.Radiobutton(f, text="Project folder", variable=self.input_mode, value="folder").pack(anchor="w")
        row += 1

        # Files
        ff = ttk.Frame(f)
        ff.pack(fill=tk.X, pady=2)
        ttk.Button(ff, text="Add file...", command=self._add_file).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(ff, text="Remove selected", command=self._remove_file).pack(side=tk.LEFT, padx=(0, 5))
        self.file_listbox = tk.Listbox(ff, height=3, width=60)
        self.file_listbox.pack(side=tk.LEFT, fill=tk.X, expand=True)
        row += 1

        # Project folder
        pf = ttk.Frame(f)
        pf.pack(fill=tk.X, pady=2)
        ttk.Label(pf, text="Project root:").pack(side=tk.LEFT, padx=(0, 5))
        ttk.Entry(pf, textvariable=self.project_root, width=50).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        ttk.Button(pf, text="Browse...", command=self._browse_folder).pack(side=tk.LEFT)
        row += 1

        pf2 = ttk.Frame(f)
        pf2.pack(fill=tk.X, pady=2)
        ttk.Label(pf2, text="Include:").pack(side=tk.LEFT, padx=(0, 5))
        ttk.Entry(pf2, textvariable=self.include_patterns, width=40).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Label(pf2, text="Exclude:").pack(side=tk.LEFT, padx=(0, 5))
        ttk.Entry(pf2, textvariable=self.exclude_patterns, width=20).pack(side=tk.LEFT)
        row += 1

        # Mode
        mf = ttk.LabelFrame(self, text="Mode", padding=5)
        mf.grid(row=row, column=0, columnspan=2, sticky="ew", pady=2)
        ttk.Combobox(
            mf,
            textvariable=self.mode,
            values=["auto", "cl", "rpg", "db2", "dspf", "combined"],
            width=15,
            state="readonly",
        ).pack(anchor="w")
        row += 1

        # Output
        of = ttk.LabelFrame(self, text="Output", padding=5)
        of.grid(row=row, column=0, columnspan=2, sticky="ew", pady=2)
        ttk.Label(of, text="Output folder:").pack(anchor="w")
        of2 = ttk.Frame(of)
        of2.pack(fill=tk.X)
        ttk.Entry(of2, textvariable=self.output_folder, width=55).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        ttk.Button(of2, text="Browse...", command=self._browse_output).pack(side=tk.LEFT)
        ttk.Checkbutton(of, text="Export PDF report", variable=self.enable_pdf).pack(anchor="w")
        row += 1

        # Email
        ef = ttk.LabelFrame(self, text="Email (optional)", padding=5)
        ef.grid(row=row, column=0, columnspan=2, sticky="ew", pady=2)
        ttk.Checkbutton(ef, text="Email report", variable=self.enable_email).pack(anchor="w")
        ef2 = ttk.Frame(ef)
        ef2.pack(fill=tk.X)
        ttk.Label(ef2, text="To:").pack(side=tk.LEFT, padx=(0, 5))
        ttk.Entry(ef2, textvariable=self.email_to, width=40).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Label(ef2, text="SMTP host:").pack(side=tk.LEFT, padx=(0, 5))
        ttk.Entry(ef2, textvariable=self.smtp_host, width=25).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Label(ef2, text="Port:").pack(side=tk.LEFT, padx=(0, 5))
        ttk.Entry(ef2, textvariable=self.smtp_port, width=6).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Checkbutton(ef2, text="TLS", variable=self.smtp_tls).pack(side=tk.LEFT, padx=(0, 5))
        ef3 = ttk.Frame(ef)
        ef3.pack(fill=tk.X)
        ttk.Label(ef3, text="User:").pack(side=tk.LEFT, padx=(0, 5))
        ttk.Entry(ef3, textvariable=self.smtp_user, width=25).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Label(ef3, text="Pass:").pack(side=tk.LEFT, padx=(0, 5))
        ttk.Entry(ef3, textvariable=self.smtp_pass, width=25, show="*").pack(side=tk.LEFT)
        row += 1

        # Run
        ttk.Button(self, text="Run Analysis", command=self._run).grid(row=row, column=0, columnspan=2, pady=10)
        row += 1

        # Log
        lf = ttk.LabelFrame(self, text="Log", padding=5)
        lf.grid(row=row, column=0, columnspan=2, sticky="nsew", pady=2)
        self.log_text = tk.Text(lf, height=12, wrap=tk.WORD, state=tk.DISABLED, font=("Courier New", 9))
        self.log_text.pack(fill=tk.BOTH, expand=True)
        sb = ttk.Scrollbar(self.log_text, command=self.log_text.yview)
        self.log_text.config(yscrollcommand=sb.set)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(row, weight=1)

    def _add_file(self) -> None:
        paths = filedialog.askopenfilenames(
            title="Select IBM i source files",
            filetypes=[
                ("All supported", "*.cl *.clle *.rpg *.rpgle *.sql *.dspf"),
                ("CL", "*.cl *.clle"),
                ("RPG", "*.rpg *.rpgle"),
                ("SQL", "*.sql"),
                ("DSPF", "*.dspf"),
                ("All files", "*.*"),
            ],
        )
        for p in paths:
            if p and p not in self.files:
                self.files.append(p)
                self.file_listbox.insert(tk.END, p)

    def _remove_file(self) -> None:
        sel = self.file_listbox.curselection()
        if sel:
            idx = sel[0]
            self.file_listbox.delete(idx)
            self.files.pop(idx)

    def _browse_folder(self) -> None:
        d = filedialog.askdirectory(title="Select project root")
        if d:
            self.project_root.set(d)

    def _browse_output(self) -> None:
        d = filedialog.askdirectory(title="Select output folder")
        if d:
            self.output_folder.set(d)

    def _log(self, msg: str) -> None:
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, msg + "\n")
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)

    def _run(self) -> None:
        inputs: list[InputSpec] = []
        if self.input_mode.get() == "files":
            inputs = [InputSpec(path=p, kind="auto") for p in self.files]
        else:
            from core.io import discover_files

            root = self.project_root.get().strip()
            if not root or not Path(root).is_dir():
                messagebox.showerror("Error", "Please select a valid project folder.")
                return
            inc = [x.strip() for x in self.include_patterns.get().split(",") if x.strip()]
            exc = [x.strip() for x in self.exclude_patterns.get().split(",") if x.strip()]
            paths = discover_files(root, include_patterns=inc, exclude_patterns=exc)
            inputs = [InputSpec(path=str(p), kind="auto") for p in paths]

        if not inputs:
            messagebox.showerror("Error", "No input files selected or discovered.")
            return

        out = self.output_folder.get().strip() or str(ROOT / "output")
        Path(out).mkdir(parents=True, exist_ok=True)

        export = None
        if self.enable_pdf.get():
            pdf_name = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
            pdf_path = str(Path(out) / pdf_name)
            smtp = None
            if self.enable_email.get() and self.email_to.get() and self.smtp_host.get():
                smtp = {
                    "host": self.smtp_host.get(),
                    "port": int(self.smtp_port.get() or 587),
                    "username": self.smtp_user.get() or None,
                    "password": self.smtp_pass.get() or None,
                    "use_tls": self.smtp_tls.get(),
                }
            export = ExportOptions(
                enable_pdf=True,
                pdf_path=pdf_path,
                enable_email=self.enable_email.get(),
                email_to=self.email_to.get() or None,
                email_subject="IBM i Analysis Report",
                email_smtp_config=smtp,
            )

        self._log(f"Starting analysis at {datetime.now().isoformat()}")
        self._log(f"Files: {len(inputs)}")
        self._log(f"Mode: {self.mode.get()}")

        def run_in_thread():
            try:
                result = run_pipeline(inputs, mode=self.mode.get(), export=export)
                self.after(0, lambda: self._on_done(result, export))
            except Exception as e:
                err_msg = str(e)
                self.after(0, lambda: self._on_error(err_msg))

        threading.Thread(target=run_in_thread, daemon=True).start()

    def _on_done(self, result, export) -> None:
        self._log(f"Completed. Diagnostics: {len(result.diagnostics)}")
        for d in result.diagnostics[:30]:
            self._log(f"  {d}")
        if len(result.diagnostics) > 30:
            self._log(f"  ... and {len(result.diagnostics) - 30} more")
        self._log(f"CL: {len(result.cl_results)}, RPG: {len(result.rpg_results)}, DB2: {len(result.db2_results)}, DSPF: {len(result.dspf_results)}")
        
        self._log("\n--- Analysis Reports ---")
        for r in result.cl_results:
            self._log(f"\n{r.summary_report}")
        for r in result.rpg_results:
            self._log(f"\n{r.summary_report}")
        for r in result.db2_results:
            self._log(f"\n{r.summary_report}")
        for r in result.dspf_results:
            self._log(f"\n{r.summary_report}")

        if export and export.enable_pdf and export.pdf_path:
            self._log(f"PDF saved to: {export.pdf_path}")
            if export.enable_email:
                self._log("Email sent.")
        messagebox.showinfo("Done", "Analysis completed. Check the log.")

    def _on_error(self, msg: str) -> None:
        self._log(f"Error: {msg}")
        messagebox.showerror("Error", msg)


if __name__ == "__main__":
    main()
