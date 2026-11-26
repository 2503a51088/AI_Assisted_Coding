"""
Multiplication Tables Generator

This module prints multiplication tables from 1 through 20.
Each table includes products for multipliers 1 through 10.
"""


def multiplication_tables():
    """
    Print multiplication tables for numbers 1 through 20.

    The function uses a nested loop. The outer loop selects numbers,
    while the inner loop multiplies each number by 1 through 10.
    """
    for number in range(1, 21):
        print(f"\nMultiplication Table of {number}")

        for multiplier in range(1, 11):
            print(f"{number} x {multiplier} = {number * multiplier}")


if __name__ == "__main__":
    multiplication_tables()