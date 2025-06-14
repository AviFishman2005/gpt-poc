import requests
from typing import Tuple, List, Dict

class ThreatIntelPlatform:
    """Simple threat intelligence platform."""
    def __init__(self):
        self.country_url = "https://isc.sans.edu/api/country?json"

    def fetch_country_data(self) -> List[Dict]:
        resp = requests.get(self.country_url, timeout=10)
        resp.raise_for_status()
        return resp.json()

    def top_attacked_country(self) -> Tuple[str, int] | None:
        data = self.fetch_country_data()
        entries = [e for e in data if e.get("country")]
        if not entries:
            return None
        top_entry = max(entries, key=lambda x: x.get("targets", 0))
        country_code = top_entry.get("country")
        targets = int(top_entry.get("targets", 0))
        return country_code, targets

    def country_flag(self, country_code: str) -> str:
        if len(country_code) != 2:
            return ""
        return "".join(chr(ord(c.upper()) + 127397) for c in country_code)

    def daily_attacked(self) -> str:
        result = self.top_attacked_country()
        if not result:
            return "No data"
        country, count = result
        return f"{country} {self.country_flag(country)} - {count} targets"

if __name__ == "__main__":
    platform = ThreatIntelPlatform()
    print(platform.daily_attacked())
