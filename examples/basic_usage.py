"""Small example using only the public modules."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from proton_no_raids_public.security_events import SecurityEvent, SecurityEventType
from proton_no_raids_public.settings_cache import GuildSettingsCache

cache = GuildSettingsCache(ttl_seconds=120)
cache.update(123456789, protection_enabled=True)

settings = cache.get(123456789)
print("settings:", settings)

event = SecurityEvent(
    guild_id=123456789,
    event_type=SecurityEventType.CONFIG_UPDATED,
    description="Public example: protection setting updated.",
)
print("event:", event.as_dict())
