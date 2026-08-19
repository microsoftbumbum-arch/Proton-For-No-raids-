# Proton for No Raids — Public Modules

Public showcase and selected utility modules from **Proton for No Raids**, a Discord security and server-protection project.

> This repository intentionally contains only a **partial public version**. The production anti-raid engine, detection rules, OCR pipeline, AI moderation prompts, database implementation, validation system and other security-sensitive logic remain private.

## What is included

- Reusable Discord embed helpers
- In-memory guild settings cache
- Safe permission/hierarchy checks
- Generic security-event models
- Example integration code
- Unit tests
- Architecture and security documentation

## What is not included

- Anti-raid detection engine and thresholds
- Anti-advertising / anti-sale detection rules
- OCR and image-analysis pipeline
- AI moderation providers, prompts and API handling
- Bot whitelist / bypass logic
- Automated punitive actions
- Production database schema and service-role access
- Server validation / access-control flow
- Owner/admin internal panels
- Production credentials or deployment secrets

## Project structure

```text
proton-for-no-raids-public/
├── src/proton_no_raids_public/
│   ├── __init__.py
│   ├── embeds.py
│   ├── permissions.py
│   ├── security_events.py
│   └── settings_cache.py
├── examples/
│   └── basic_usage.py
├── tests/
│   ├── test_security_events.py
│   └── test_settings_cache.py
├── docs/
│   └── ARCHITECTURE.md
├── .env.example
├── .gitignore
├── CHANGELOG.md
├── LICENSE
├── SECURITY.md
└── requirements.txt
```

## Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run the tests:

```bash
python -m unittest discover -s tests -v
```

## About the production project

The full Proton for No Raids project is designed around Discord server protection, configurable security modules, logging and automated monitoring. This public repository is intended for portfolio/reference purposes and does **not** contain the complete production bot.

## Security

Never commit `.env`, Discord bot tokens, Supabase service-role keys, API keys or database credentials. See [SECURITY.md](SECURITY.md).
