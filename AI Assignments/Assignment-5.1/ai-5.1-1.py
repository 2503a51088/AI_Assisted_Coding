"""Weather API example: insecure AI output versus a secure revision.

Install the dependency with: python -m pip install requests
Set WEATHER_API_KEY before running the secure example.
"""

import os
import json
from urllib.parse import urlencode
from urllib.request import urlopen


# Original AI-generated version: do not use this pattern in production.
# The key is embedded in source code and could be exposed in source control.
def fetch_weather_insecure(city: str) -> dict:
	api_key = "YOUR_API_KEY_HERE"
	query = urlencode({"q": city, "appid": api_key, "units": "metric"})
	with urlopen(
		f"https://api.openweathermap.org/data/2.5/weather?{query}", timeout=10
	) as response:
		return json.load(response)


# Secure revision: keep the key outside the source code.
def fetch_weather(city: str) -> dict:
	api_key = os.environ.get("WEATHER_API_KEY")
	if not api_key:
		raise RuntimeError(
			"WEATHER_API_KEY is not set. Configure it in the environment."
		)

	query = urlencode({"q": city, "appid": api_key, "units": "metric"})
	with urlopen(
		f"https://api.openweathermap.org/data/2.5/weather?{query}", timeout=10
	) as response:
		return json.load(response)


if __name__ == "__main__":
	city = input("City: ").strip()
	weather = fetch_weather(city)
	print(f"{weather['name']}: {weather['main']['temp']} C")

