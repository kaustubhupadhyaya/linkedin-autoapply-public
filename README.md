# LinkedIn Auto Job Applier (public fork)

A Selenium bot that searches LinkedIn for jobs, fills Easy Apply forms, and records what it applied to. It is a cleaned public copy of a private fork of [GodsScion/Auto_job_applier_linkedIn](https://github.com/GodsScion/Auto_job_applier_linkedIn).

The upstream project and its contributors keep their copyright. This fork keeps the GNU Affero General Public License v3.0. See `LICENSE` and `NOTICE`.

## Live-account risk

This software drives a real LinkedIn account through a browser. Automated activity can get an account restricted, challenged, or banned. LinkedIn's terms restrict scraping and automation. You run it at your own risk.

Read these before the first live run:

- Run `python runAiBot.py` once with `pause_before_submit = True` and `pause_at_failed_question = True` in `config/questions.py`. Watch every step.
- Start with a small search and a low `switch_number` in `config/search.py`.
- Do not run it in CI, on a schedule, or on an account you cannot afford to lose.
- The CI workflow here only byte-compiles the code. It never opens a browser.

## Requirements

- Python 3.10 or newer
- Google Chrome in its default install location
- Windows, Linux, or macOS. The supervisor is written for Windows.

## Setup

1. Clone the repository and enter it.

2. Create a virtual environment and install the runtime dependencies.

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
   ```

3. Create your local configuration from the examples. Both real files are git-ignored.

   ```powershell
   Copy-Item config\personals.example.py config\personals.py
   Copy-Item config\questions.example.py config\questions.py
   ```

   Edit `config/personals.py` with your own details. Edit `config/questions.py` with your resume path, work authorization, salary expectations, and answer preferences. Review `config/search.py` and `config/settings.py`.

4. Set credentials through environment variables. Do not put them in a tracked file.

   ```powershell
   $env:LINKEDIN_USERNAME = "your sign-in name"
   $env:LINKEDIN_PASSWORD = "your password"
   ```

   Optional AI answers:

   ```powershell
   $env:LINKEDIN_USE_AI = "true"
   $env:LINKEDIN_AI_PROVIDER = "openai"   # openai, deepseek, gemini or proxy
   $env:LLM_API_KEY = "your provider key"
   $env:LLM_API_URL = "https://api.openai.com/v1"
   $env:LLM_MODEL = "gpt-4o-mini"
   ```

   `config/secrets.py` reads those variables. It also supports an optional local vault. Set `SECURE_VAULT_PATH` to the directory that contains the vault library, and `LINKEDIN_VAULT_LABEL` to the entry label. The vault is read in process and its values are never printed.

5. Run the bot.

   ```powershell
   .\.venv\Scripts\python.exe runAiBot.py
   ```

   The hardened local runner adds resilient logging, session recovery, security-wall detection, and safer answer handling:

   ```powershell
   .\.venv\Scripts\python.exe run_linkedin_local.py
   ```

   The supervisor restarts the local runner after a crash and stops on a verification wall, a sign-in failure, or repeated zero-apply runs:

   ```powershell
   .\.venv\Scripts\python.exe run_linkedin_supervised.py
   ```

6. Optional applied-jobs UI:

   ```powershell
   .\.venv\Scripts\python.exe app.py
   ```

   Open `http://localhost:5000`.

## Optional local integrations

The fork was written with a private job tracker and a private knowledge module. Both are optional. Without them the bot keeps its built-in behavior.

| Variable | Purpose |
| --- | --- |
| `LINKEDIN_FIT_RULES_PY` | Path to a Python module that exports `load_rules()` and `title_reasons()`. |
| `LINKEDIN_FIT_RULES_JSON` | Path to the matching rules JSON file. |
| `JOB_TRACKER_DIR` | Directory of an optional tracker package used for outage toasts. |
| `JOB_TRACKER_TRACKER` | Path to a tracker script used for reconciliation. |
| `CANDIDATE_KNOWLEDGE_MODULE` | Path to a module that grounds AI answers in verified candidate facts. |
| `LINKEDIN_PYTHON` | Interpreter the supervisor uses for the child process. Defaults to the current interpreter. |

If `LINKEDIN_FIT_RULES_PY` or its JSON file is missing, the local runner logs a note and continues without the title gate.

## What not to commit

The `.gitignore` excludes the real `config/personals.py`, `config/questions.py`, `.env`, `login.txt`, logs, resumes, spreadsheets, browser profiles, and virtual environments. Keep it that way.

The public copy contains no personal configuration, credentials, application history, resumes, or browser profiles.

## Fork changes

- Environment and optional vault credential loading instead of hard-coded secrets.
- Hardened local runner with resilient logging, session recovery, security-wall evidence, and safer form answers.
- Supervised runner with restart limits, memory checks, and network-outage handling.
- Optional title gate, job tracker, and candidate knowledge integrations through environment variables.
- Sanitized configuration examples and a public-release cleanup.

See `NOTICE` for attribution and the full change summary.

## License

GNU Affero General Public License v3.0. See `LICENSE`.
