import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from proton_no_raids_public.security_events import SecurityEvent, SecurityEventType


class SecurityEventTests(unittest.TestCase):
    def test_serialization(self):
        event = SecurityEvent(
            guild_id=10,
            event_type=SecurityEventType.CONFIG_UPDATED,
            description="updated",
            actor_id=20,
        )
        data = event.as_dict()
        self.assertEqual(data["guild_id"], 10)
        self.assertEqual(data["event_type"], "config_updated")
        self.assertEqual(data["actor_id"], 20)
        self.assertIn("created_at", data)


if __name__ == "__main__":
    unittest.main()
