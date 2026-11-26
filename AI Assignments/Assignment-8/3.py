import requests  # Send HTTP requests to the weather service


GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"  # City search endpoint
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"  # Weather data endpoint


def get_weather(city):
    """Find a city and return its current weather information."""
    location_response = requests.get(  # Search for the entered city
        GEOCODING_URL,
        params={"name": city, "count": 1, "language": "en", "format": "json"},
        timeout=10
    )
    locations = location_response.json().get("results", [])  # Get matching locations

    if not locations:  # Check whether the city exists
        return None  # Return no data when no location is found

    location = locations[0]  # Select the first matching location
    weather_response = requests.get(  # Request the city's current weather
        WEATHER_URL,
        params={
            "latitude": location["latitude"],  # Use the city's latitude
            "longitude": location["longitude"],  # Use the city's longitude
            "current": "temperature_2m,relative_humidity_2m,weather_code",  # Requested values
            "timezone": "auto"  # Use local time for the city
        },
        timeout=10
    )
    weather_data = weather_response.json()["current"]  # Get current weather data

    return {  # Return the formatted weather information
        "city": location["name"],
        "temperature_celsius": weather_data["temperature_2m"],
        "humidity_percent": weather_data["relative_humidity_2m"],
        "weather_code": weather_data["weather_code"]
    }


if __name__ == "__main__":  # Run when the file is executed
    city_name = input("Enter a city name: ")  # Ask the user for a city
    weather = get_weather(city_name)  # Fetch the current weather

    if weather:  # Check whether weather data was found
        print(f"\nWeather in {weather['city']}")  # Print the city name
        print(f"Temperature: {weather['temperature_celsius']} C")  # Print temperature
        print(f"Humidity: {weather['humidity_percent']}%")  # Print humidity
        print(f"Weather code: {weather['weather_code']}")  # Print weather code
    else:  # Handle an unknown city
        print("City not found.")  # Print an error message