# Few-shot examples for the prompt:
# is_prime(2)  -> True
# is_prime(3)  -> True
# is_prime(4)  -> False
# is_prime(1)  -> False
# is_prime(0)  -> False
# is_prime(17) -> True
# is_prime(18) -> False


def is_prime(number):
	"""Return True when number is prime, otherwise return False."""
	if number < 2:
		return False
	if number == 2:
		return True
	if number % 2 == 0:
		return False

	divisor = 3
	while divisor * divisor <= number:
		if number % divisor == 0:
			return False
		divisor += 2
	return True


if __name__ == "__main__":
	examples = [2, 3, 4, 1, 0, 17, 18]
	for number in examples:
		print(f"is_prime({number}) -> {is_prime(number)}")
