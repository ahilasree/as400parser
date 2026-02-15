"""
Optional email sending for pipeline PDF reports.

Uses Python standard smtplib and email modules.
"""

import logging
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import ExportOptions

logger = logging.getLogger(__name__)


def send_pipeline_pdf_via_email(pdf_path: str, export: "ExportOptions") -> None:
    """
    Send the generated PDF as an email attachment using SMTP config.

    Only sends if export.enable_email, export.email_to, and export.email_smtp_config
    are set. Credentials come from ExportOptions; no hardcoded secrets.
    """
    if not export.enable_email or not export.email_to:
        return
    cfg = export.email_smtp_config
    if not cfg or not cfg.get("host"):
        logger.warning("SMTP config missing; skipping email")
        return

    pdf = Path(pdf_path)
    if not pdf.exists():
        logger.warning("PDF file not found: %s", pdf_path)
        return

    msg = MIMEMultipart()
    msg["Subject"] = export.email_subject or "IBM i Analysis Report"
    msg["From"] = cfg.get("username", cfg.get("from", "noreply@local"))
    msg["To"] = export.email_to

    msg.attach(MIMEText("Please find the IBM i analysis report attached.", "plain"))
    with open(pdf, "rb") as f:
        part = MIMEApplication(f.read(), _subtype="pdf")
        part.add_header("Content-Disposition", "attachment", filename=pdf.name)
        msg.attach(part)

    try:
        use_tls = cfg.get("use_tls", True)
        port = cfg.get("port", 587)
        with smtplib.SMTP(cfg["host"], port) as smtp:
            if use_tls:
                smtp.starttls()
            if cfg.get("username") and cfg.get("password"):
                smtp.login(cfg["username"], cfg["password"])
            smtp.send_message(msg)
        logger.info("Email sent to %s", export.email_to)
    except Exception as e:
        logger.exception("Failed to send email: %s", e)
        raise
