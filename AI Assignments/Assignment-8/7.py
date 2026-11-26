"""Generate multiplication tables from 1 through 30."""


def multiplication_tables():
    """Print multiplication tables for numbers from 1 through 30.

    Args:
        None.

    Returns:
        None: The tables are printed directly to standard output.
    """
    for number in range(1, 31):  # Loop through numbers 1 to 30
        print(f"\nMultiplication Table of {number}")  # Display the table heading

        for multiplier in range(1, 11):  # Loop through multipliers 1 to 10
            print(f"{number} x {multiplier} = {number * multiplier}")  # Print one multiplication


if __name__ == "__main__":
    multiplication_tables()  # Run the program