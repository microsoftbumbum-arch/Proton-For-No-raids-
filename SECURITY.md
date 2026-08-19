# Security Policy

## Secrets

Do not open issues or commits containing production credentials. Never commit:

- Discord bot tokens
- Supabase service-role keys
- API keys
- database passwords or connection strings
- private moderation prompts or internal bypass rules

If a credential is exposed, revoke/rotate it immediately.

## Scope of this repository

This repository contains only non-sensitive public modules. Reports about the private production anti-raid implementation should not include exploit details in public issues.
