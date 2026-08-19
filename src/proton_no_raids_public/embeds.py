"""Presentation helpers for Discord embeds."""

from __future__ import annotations

import discord

DEFAULT_COLOR = 0x111111


def create_embed(*, title: str | None = None, description: str | None = None, color: int = DEFAULT_COLOR) -> discord.Embed:
    embed = discord.Embed(title=title, description=description, color=color)
    embed.set_footer(text="Proton for No Raids • Public showcase")
    return embed
