import unittest
from threat_intel.platform import ThreatIntelPlatform

class TestThreatIntelPlatform(unittest.TestCase):
    def setUp(self):
        self.platform = ThreatIntelPlatform()

    def test_top_attacked_country_returns_tuple(self):
        result = self.platform.top_attacked_country()
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        country, count = result
        self.assertIsInstance(country, str)
        self.assertTrue(country)
        self.assertIsInstance(count, int)

    def test_country_flag(self):
        self.assertEqual(self.platform.country_flag('US'), '\U0001F1FA\U0001F1F8')

if __name__ == '__main__':
    unittest.main()
