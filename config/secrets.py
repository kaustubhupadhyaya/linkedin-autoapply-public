'''
Author:     Sai Vignesh Golla
LinkedIn:   https://www.linkedin.com/in/saivigneshgolla/

Copyright (C) 2024 Sai Vignesh Golla

License:    GNU Affero General Public License
            https://www.gnu.org/licenses/agpl-3.0.en.html

GitHub:     https://github.com/GodsScion/Auto_job_applier_linkedIn

version:    24.12.3.10.30
'''


###################################################### CONFIGURE YOUR TOOLS HERE ######################################################

# Credentials come from environment variables. Nothing secret belongs in this file.
#
#   LINKEDIN_USERNAME      LinkedIn sign-in email or phone
#   LINKEDIN_PASSWORD      LinkedIn password
#   LINKEDIN_USE_AI        "true" or "false" (default: false)
#   LINKEDIN_AI_PROVIDER   "openai", "deepseek", "gemini" or "proxy"
#   LLM_API_KEY            API key for the selected provider (not needed for "proxy")
#   LLM_API_URL            API base URL
#   LLM_MODEL              model name
#
# Optional vault support: set SECURE_VAULT_PATH to a directory that contains
# vault.py, and LINKEDIN_VAULT_LABEL to the vault entry label (default
# "linkedin-1"). The vault is used only when the matching env var is empty.
#
# See config/secrets.example.py for a commented template.
import os
import sys


def _env(name: str, default: str = "") -> str:
    return os.environ.get(name, default).strip()


def _env_bool(name: str, default: bool = False) -> bool:
    raw = _env(name)
    if not raw:
        return default
    return raw.lower() in ("1", "true", "yes", "on")


def _from_vault(field: str) -> str:
    """Read one field from the optional secure-vault. Never logs the value."""
    vault_path = _env("SECURE_VAULT_PATH")
    if not vault_path:
        return ""
    label = _env("LINKEDIN_VAULT_LABEL", "linkedin-1") or "linkedin-1"
    try:
        if vault_path not in sys.path:
            sys.path.insert(0, vault_path)
        import vault as _vault
        return _vault.get_secret(label, field) or ""
    except Exception as exc:
        print(f"[secrets] secure-vault not available ({type(exc).__name__}); using environment variables.", flush=True)
        return ""


## Login Credentials for LinkedIn
username = _env("LINKEDIN_USERNAME") or _from_vault("email")
password = _env("LINKEDIN_PASSWORD") or _from_vault("password")
if not username or not password:
    raise RuntimeError(
        "LinkedIn credentials are not set. Set LINKEDIN_USERNAME and LINKEDIN_PASSWORD "
        "in the environment, or configure SECURE_VAULT_PATH and LINKEDIN_VAULT_LABEL. "
        "See README.md."
    )


## Artificial Intelligence (optional)
# Use AI
use_AI = _env_bool("LINKEDIN_USE_AI", False)

# Select AI provider
ai_provider = _env("LINKEDIN_AI_PROVIDER", "openai") or "openai"

# Model and endpoint (non-secret)
llm_model = _env("LLM_MODEL", "gpt-4o-mini") or "gpt-4o-mini"
llm_api_url = _env("LLM_API_URL", "https://api.openai.com/v1") or "https://api.openai.com/v1"

# API key (secret). Empty is allowed when use_AI is False or the provider is "proxy".
llm_api_key = _env("LLM_API_KEY")

llm_spec = "openai"

# Do you want to stream AI output?
stream_output = _env_bool("LLM_STREAM_OUTPUT", False)


############################################################################################################
'''
Upstream project: https://github.com/GodsScion/Auto_job_applier_linkedIn
License: GNU Affero General Public License v3.0
'''
############################################################################################################
