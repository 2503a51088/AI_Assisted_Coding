"""
Random Number Guessing Game

This module contains a simple number guessing game using Python's
random module.
"""

import random


def play_guessing_game():
    """
    Run the random number guessing game.

    The program selects a random number from 1 through 100. The user
    continues guessing until the correct number is entered.
    """
    secret_number = random.randint(1, 100)

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the correct number.")
            break


if __name__ == "__main__":
    play_guessing_game()