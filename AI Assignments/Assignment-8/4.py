"""Print multiplication tables for numbers from 1 to 30."""


def print_multiplication_tables(start=1, end=30, multiplier_end=10):
    """Print multiplication tables for a range of numbers.

    Args:
        start: The first number whose table will be printed.
        end: The last number whose table will be printed.
        multiplier_end: The highest multiplier used in each table.

    Returns:
        None.
    """
    if start > end:
        raise ValueError("Start must be less than or equal to end.")

    for number in range(start, end + 1):
        print(f"\nMultiplication table of {number}")
        for multiplier in range(1, multiplier_end + 1):
            print(f"{number} x {multiplier} = {number * multiplier}")


if __name__ == "__main__":
    print_multiplication_tables()