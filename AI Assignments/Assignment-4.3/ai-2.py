def centimeters_to_inches(centimeters: float) -> float:
	"""Convert centimeters to inches using 1 inch = 2.54 centimeters."""
	if not isinstance(centimeters, (int, float)) or isinstance(centimeters, bool):
		raise TypeError("centimeters must be a number")
	if centimeters < 0:
		raise ValueError("centimeters must not be negative")

	return round(centimeters / 2.54, 2)


if __name__ == "__main__":
	try:
		centimeters = float(input("Enter length in centimeters: "))
		inches = centimeters_to_inches(centimeters)
		print(f"{centimeters:g} cm = {inches:.2f} inches")
	except (TypeError, ValueError) as error:
		print(f"Error: {error}")
