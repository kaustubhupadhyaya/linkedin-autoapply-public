'''
Author:     Sai Vignesh Golla
LinkedIn:   https://www.linkedin.com/in/saivigneshgolla/

Copyright (C) 2024 Sai Vignesh Golla

License:    GNU Affero General Public License
            https://www.gnu.org/licenses/agpl-3.0.en.html

GitHub:     https://github.com/GodsScion/Auto_job_applier_linkedIn

version:    24.12.3.10.30
'''


###################################################### EXAMPLE CREDENTIALS ######################################################

# This file is a template only. The repository ships config/secrets.py, which
# reads the real values from environment variables and never stores them.
# Copy this file to config/secrets.py only if you prefer a static local file,
# and never commit the result.
#
# Recommended: leave config/secrets.py in place and set these environment
# variables instead.
#
#   LINKEDIN_USERNAME
#   LINKEDIN_PASSWORD
#   LINKEDIN_USE_AI
#   LINKEDIN_AI_PROVIDER
#   LLM_API_KEY
#   LLM_API_URL
#   LLM_MODEL
#
# Optional secure-vault support: set SECURE_VAULT_PATH and
# LINKEDIN_VAULT_LABEL, then leave the env values empty. The vault is read in
# process; its contents are never printed or written to disk.


# Login Credentials for LinkedIn
username = "YOUR_LINKEDIN_EMAIL"
password = "YOUR_LINKEDIN_PASSWORD"


## Artificial Intelligence (optional)
# Use AI
use_AI = False

# Select AI provider: "openai", "deepseek", "gemini" or "proxy"
ai_provider = "openai"

# Model and endpoint (non-secret)
llm_model = "gpt-4o-mini"
llm_api_url = "https://api.openai.com/v1"

# API key (secret). Empty is allowed when use_AI is False or provider is "proxy".
llm_api_key = ""

llm_spec = "openai"

# Do you want to stream AI output?
stream_output = False


############################################################################################################
'''
Upstream project: https://github.com/GodsScion/Auto_job_applier_linkedIn
License: GNU Affero General Public License v3.0
'''
############################################################################################################
