import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from proton_no_raids_public.settings_cache import GuildSettingsCache


class FakeClock:
    def __init__(self):
        self.value = 1000.0
    def __call__(self):
        return self.value


class GuildSettingsCacheTests(unittest.TestCase):
    def test_update_and_get(self):
        clock = FakeClock()
        cache = GuildSettingsCache(ttl_seconds=10, clock=clock)
        cache.update(1, protection_enabled=True)
        self.assertTrue(cache.get(1).protection_enabled)

    def test_expires(self):
        clock = FakeClock()
        cache = GuildSettingsCache(ttl_seconds=10, clock=clock)
        cache.update(1, protection_enabled=True)
        clock.value += 11
        self.assertIsNone(cache.get(1))

    def test_unknown_setting_rejected(self):
        cache = GuildSettingsCache()
        with self.assertRaises(KeyError):
            cache.update(1, hidden_rule=True)


if __name__ == "__main__":
    unittest.main()
