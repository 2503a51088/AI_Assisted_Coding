"""A simple command-line calculator with documented functions."""


def calculate(number1, number2, operation):
    """Calculate a result using two numbers and an arithmetic operation.

    Args:
        number1: The first number.
        number2: The second number.
        operation: The arithmetic operator: '+', '-', '*', or '/'.

    Returns:
        The result of the calculation.

    Raises:
        ValueError: If the operation is invalid.
        ZeroDivisionError: If division by zero is attempted.
    """
    if operation == "+":
        return number1 + number2
    if operation == "-":
        return number1 - number2
    if operation == "*":
        return number1 * number2
    if operation == "/":
        return number1 / number2
    raise ValueError("Invalid operation.")


def main():
    """Read calculator input from the user and display the result."""
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    operation = input("Enter operation (+, -, *, /): ")

    try:
        result = calculate(number1, number2, operation)
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()