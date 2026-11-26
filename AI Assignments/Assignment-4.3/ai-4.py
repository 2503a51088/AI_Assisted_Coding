"""Compare zero-shot and few-shot approaches for counting vowels."""


def count_vowels_zero_shot(text: str) -> int:
	"""Return the number of vowels in text."""
	vowel_count = 0
	for character in text.lower():
		if character in "aeiou":
			vowel_count += 1
	return vowel_count


def count_vowels_few_shot(text: str) -> int:
	"""Return the number of vowels in text.

	The intended behavior is illustrated by these examples:
	- "Hello" contains 2 vowels.
	- "Python" contains 1 vowel.
	- "AEIOU" contains 5 vowels.
	"""
	vowels = {"a", "e", "i", "o", "u"}
	return sum(character in vowels for character in text.lower())


def compare_approaches():
	"""Print a short comparison of both generated approaches."""
	print("Zero-shot result:", count_vowels_zero_shot("Hello Python"))
	print("Few-shot result: ", count_vowels_few_shot("Hello Python"))
	print("\nComparison")
	print("Accuracy: Both functions correctly count uppercase and lowercase vowels.")
	print("Readability: The zero-shot version is more explicit; the few-shot version is more concise.")
	print("Logical clarity: The zero-shot loop shows each counting step, while the few-shot version clearly separates vowels from other characters.")


if __name__ == "__main__":
	text = input("Enter a string: ")
	print(f"Zero-shot count: {count_vowels_zero_shot(text)}")
	print(f"Few-shot count: {count_vowels_few_shot(text)}")
	compare_approaches()
