def sum_even_and_odd(numbers: list[int]) -> tuple[int, int]:
    """Calculate the sums of the even and odd numbers in a list.

    Args:
        numbers: A list of integers to process.

    Returns:
        A tuple containing the sum of the even numbers followed by the sum
        of the odd numbers. If either group is empty, its sum is 0.
    """
    even_sum = sum(number for number in numbers if number % 2 == 0)
    odd_sum = sum(number for number in numbers if number % 2 != 0)
    return even_sum, odd_sum


if __name__ == "__main__":
    even_total, odd_total = sum_even_and_odd([1, 2, 3, 4, 5])
    print(f"Sum of even numbers: {even_total}")
    print(f"Sum of odd numbers: {odd_total}")