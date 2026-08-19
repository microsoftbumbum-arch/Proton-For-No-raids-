"""Small TTL cache for per-guild public settings examples."""

from __future__ import annotations

import time
from dataclasses import dataclass, replace
from typing import Callable


@dataclass(frozen=True)
class GuildSettings:
    protection_enabled: bool = False
    logging_enabled: bool = True
    notifications_enabled: bool = True


class GuildSettingsCache:
    def __init__(self, ttl_seconds: float = 120.0, clock: Callable[[], float] = time.time):
        if ttl_seconds <= 0:
            raise ValueError("ttl_seconds must be greater than zero")
        self.ttl_seconds = float(ttl_seconds)
        self._clock = clock
        self._data: dict[int, tuple[GuildSettings, float]] = {}

    def get(self, guild_id: int) -> GuildSettings | None:
        item = self._data.get(int(guild_id))
        if item is None:
            return None
        settings, created_at = item
        if self._clock() - created_at > self.ttl_seconds:
            self.invalidate(guild_id)
            return None
        return settings

    def set(self, guild_id: int, settings: GuildSettings) -> GuildSettings:
        self._data[int(guild_id)] = (settings, self._clock())
        return settings

    def update(self, guild_id: int, **changes: bool) -> GuildSettings:
        current = self.get(guild_id) or GuildSettings()
        allowed = {"protection_enabled", "logging_enabled", "notifications_enabled"}
        unknown = set(changes) - allowed
        if unknown:
            raise KeyError(f"Unknown settings: {', '.join(sorted(unknown))}")
        updated = replace(current, **changes)
        return self.set(guild_id, updated)

    def invalidate(self, guild_id: int) -> None:
        self._data.pop(int(guild_id), None)

    def clear(self) -> None:
        self._data.clear()
