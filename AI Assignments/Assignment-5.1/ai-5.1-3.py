def is_armstrong_number(number: int) -> bool:
	"""Return True when number equals the sum of its digits' powers.

	For example, 153 is an Armstrong number because:
	1**3 + 5**3 + 3**3 = 153.
	"""
	if not isinstance(number, int) or isinstance(number, bool):
		raise TypeError("number must be an integer")
	if number < 0:
		return False

	# The number of digits determines the power used for every digit.
	digits = str(number)
	digit_power = len(digits)
	digit_sum = sum(int(digit) ** digit_power for digit in digits)

	# An Armstrong number is equal to this calculated digit sum.
	return digit_sum == number


if __name__ == "__main__":
	for value in (0, 153, 370, 371, 407, 123):
		result = "is" if is_armstrong_number(value) else "is not"
		print(f"{value} {result} an Armstrong number.")
