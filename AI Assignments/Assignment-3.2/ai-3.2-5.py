"""Convert distances between kilometers and miles."""

KILOMETERS_TO_MILES = 0.621371
MILES_TO_KILOMETERS = 1.609344


def kilometers_to_miles(kilometers):
	"""Return a distance converted from kilometers to miles."""
	return kilometers * KILOMETERS_TO_MILES


def miles_to_kilometers(miles):
	"""Return a distance converted from miles to kilometers."""
	return miles * MILES_TO_KILOMETERS


def convert_distance(value, from_unit, to_unit):
	"""Convert value between km/kilometers and mi/miles."""
	units = {
		"km": "km",
		"kilometer": "km",
		"kilometers": "km",
		"mi": "mi",
		"mile": "mi",
		"miles": "mi",
	}

	try:
		source = units[from_unit.strip().lower()]
		target = units[to_unit.strip().lower()]
	except (AttributeError, KeyError):
		raise ValueError("Units must be km/kilometers or mi/miles.") from None

	if source == target:
		return float(value)
	if source == "km":
		return kilometers_to_miles(float(value))
	return miles_to_kilometers(float(value))


def main():
	print("Distance Converter")
	print("Supported units: km (kilometers) and mi (miles)")

	try:
		value = float(input("Enter the distance: "))
		from_unit = input("Convert from (km or mi): ")
		to_unit = input("Convert to (km or mi): ")
		result = convert_distance(value, from_unit, to_unit)
		print(f"Result: {result:.2f} {to_unit.strip().lower()}")
	except ValueError as error:
		print(f"Error: {error}")


if __name__ == "__main__":
	main()
