# Progressive Prompt 1: calculator
# Progressive Prompt 2: Add comments explaining each operation.
# Progressive Prompt 3: Add usage examples for the calculator.


def calculator_v1(first_number, second_number, operation):
	"""Initial version: supports only addition and subtraction."""
	if operation == "+":
		return first_number + second_number
	if operation == "-":
		return first_number - second_number
	return "Invalid operation"


def calculator(first_number, second_number, operation):
	"""Improved version: supports four operations and handles errors."""
	operations = {
		"+": first_number + second_number,
		"-": first_number - second_number,
		"*": first_number * second_number,
	}

	if operation == "/":
		if second_number == 0:
			return "Cannot divide by zero"
		return first_number / second_number
	if operation in operations:
		return operations[operation]
	return "Invalid operation"


if __name__ == "__main__":
	print("Initial calculator:", calculator_v1(10, 5, "+"))
	print("Improved calculator:", calculator(10, 5, "+"))
	print("Improved multiplication:", calculator(10, 5, "*"))
	print("Improved division:", calculator(10, 5, "/"))
	print("Improved error handling:", calculator(10, 0, "/"))
