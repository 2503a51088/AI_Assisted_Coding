"""Calculate the factorial of a non-negative integer."""


def factorial(number):
    """Calculate the factorial of a non-negative integer.

    Args:
        number (int): The integer whose factorial will be calculated.

    Returns:
        int: The factorial of the given number.

    Raises:
        ValueError: If the number is negative.
    """
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    result = 1
    for value in range(2, number + 1):
        result *= value
    return result


def main():
    """Read an integer, calculate its factorial, and display the result.

    Raises:
        ValueError: If the user enters an invalid integer or negative number.
    """
    try:
        number = int(input("Enter a non-negative integer: "))
        print(f"The factorial of {number} is {factorial(number)}")
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()