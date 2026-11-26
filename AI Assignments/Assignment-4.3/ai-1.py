def is_leap_year(year: int) -> bool:
	"""Return True when year is a valid Gregorian leap year."""
	if not isinstance(year, int) or isinstance(year, bool):
		raise TypeError("year must be an integer")
	if year < 1:
		raise ValueError("year must be greater than zero")

	return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


if __name__ == "__main__":
	try:
		year = int(input("Enter a year: "))
		result = "a leap year" if is_leap_year(year) else "not a leap year"
		print(f"{year} is {result}.")
	except (TypeError, ValueError) as error:
		print(f"Error: {error}")
