"""
Random Number Generator

This module generates random integers between 1 and 100.
"""

import random


def generate_random_number():
    """
    Generate and return a random integer.

    The generated number is inclusive of both 1 and 100.

    Returns:
        int: A random integer from 1 through 100.
    """
    return random.randint(1, 100)


def main():
    """Generate and display a random number from 1 through 100."""
    number = generate_random_number()
    print(f"Random number: {number}")


if __name__ == "__main__":
    main()