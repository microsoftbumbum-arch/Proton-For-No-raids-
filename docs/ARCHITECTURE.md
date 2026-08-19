# Public Architecture Overview

The production project is organized as a Discord bot with separate layers for commands/views, persistence, monitoring and security modules.

This public edition exposes only low-risk building blocks:

1. **Settings cache** — demonstrates multi-server state handling with expiration.
2. **Permission helpers** — checks whether a bot can safely manage a target without performing destructive actions.
3. **Security events** — generic typed representation of security-related events for logging/UI.
4. **Embed helpers** — reusable presentation layer for Discord messages.

## Private production layers

The following are intentionally excluded: detection heuristics, OCR, AI classifiers, automated enforcement, threat scoring, bypass/whitelist rules, private database schemas, validation flows and internal owner controls.

This separation allows the project to be demonstrated publicly without publishing details that would make the security system easier to evade.
