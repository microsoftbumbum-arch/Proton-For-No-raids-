"""Non-destructive Discord permission and hierarchy helpers."""

from __future__ import annotations

from typing import Protocol


class RoleLike(Protocol):
    position: int


class MemberLike(Protocol):
    id: int
    top_role: RoleLike


def can_manage_member(*, bot_member: MemberLike, target: MemberLike, guild_owner_id: int) -> bool:
    """Return whether hierarchy permits managing a member.

    This helper performs no moderation action. It only demonstrates a safe
    precondition check used by Discord bots.
    """
    if target.id == guild_owner_id:
        return False
    if target.id == bot_member.id:
        return False
    return bot_member.top_role.position > target.top_role.position
