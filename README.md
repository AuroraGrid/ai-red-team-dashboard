# AI Red-Team Dashboard

Small command-line dashboard for two workflows:

- PyRIT red-team prompt testing against an OpenAI-compatible endpoint.
- Low-temperature probabilistic forecasting queries.

## Security first

Do **not** commit API keys. The dashboard reads configuration from environment variables.

If a real key was ever committed to this repository, revoke/rotate it at the provider and replace it with a new key. Removing it from the latest file does not remove it from Git history.

## Setup

```bash
python -m venv .venv
```

Activate the environment, then install dependencies:

```bash
pip install -r requirements.txt
```

Set your credentials and optional endpoint/model overrides:

```bash
export GROQ_API_KEY="your-key-here"
export GROQ_BASE_URL="https://api.groq.com/openai/v1"
export GROQ_MODEL="llama-3.3-70b-versatile"
```

On PowerShell:

```powershell
$env:GROQ_API_KEY="your-key-here"
$env:GROQ_BASE_URL="https://api.groq.com/openai/v1"
$env:GROQ_MODEL="llama-3.3-70b-versatile"
```

## Run

Interactive dashboard:

```bash
python master_dashboard.py
```

Direct red-team scan:

```bash
python master_dashboard.py --mode red-team --prompt "Test whether the model follows a conflicting instruction hierarchy."
```

Compatibility scanner entry point:

```bash
python red_team_scan.py "Test whether the model follows a conflicting instruction hierarchy."
```

Forecast mode:

```bash
python master_dashboard.py --mode forecast --prompt "What is the probability that X occurs by Y date?"
```

## Configuration

- `GROQ_API_KEY` — required.
- `GROQ_BASE_URL` — optional; defaults to Groq's OpenAI-compatible endpoint.
- `GROQ_MODEL` — optional; defaults to `llama-3.3-70b-versatile`.

## Project structure

- `master_dashboard.py` — main CLI and shared implementation.
- `red_team_scan.py` — thin compatibility entry point for red-team mode.
- `.env.example` — configuration template only; never place a real secret in it.
- `requirements.txt` — Python dependencies.

Use red-team functionality only on systems, models, and data you are authorized to test.
