"""Calculate the factorial of a non-negative integer."""


def factorial(number):
    """Calculate and return the factorial of a non-negative integer.

    Args:
        number: The non-negative integer whose factorial is calculated.

    Returns:
        The factorial of the given number.

    Raises:
        ValueError: If number is negative.
    """
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    result = 1
    for value in range(2, number + 1):
        result *= value
    return result


def main():
    """Read a number and display its factorial."""
    try:
        number = int(input("Enter a non-negative integer: "))
        print(f"The factorial of {number} is {factorial(number)}")
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()