"""Generic event types used by examples and logging interfaces."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Mapping, Any


class SecurityEventType(str, Enum):
    MEMBER_JOIN = "member_join"
    MESSAGE_FLAGGED = "message_flagged"
    PERMISSION_CHANGE = "permission_change"
    CONFIG_UPDATED = "config_updated"


@dataclass(frozen=True)
class SecurityEvent:
    guild_id: int
    event_type: SecurityEventType
    description: str
    actor_id: int | None = None
    target_id: int | None = None
    metadata: Mapping[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def as_dict(self) -> dict[str, Any]:
        return {
            "guild_id": self.guild_id,
            "event_type": self.event_type.value,
            "description": self.description,
            "actor_id": self.actor_id,
            "target_id": self.target_id,
            "metadata": dict(self.metadata),
            "created_at": self.created_at.isoformat(),
        }
