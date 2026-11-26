def quick_sort(values: list[int]) -> list[int]:
	"""Return a sorted copy of values using the QuickSort algorithm.

	Steps:
	1. Choose the middle value as a pivot.
	2. Split the input into values less than, equal to, and greater than it.
	3. Recursively sort the less-than and greater-than groups.
	4. Join the sorted groups around the pivot values.

	This implementation creates new lists, so it does not modify the input.
	Its average time complexity is O(n log n), although a poor pivot can
	make the worst case O(n**2).
	"""
	if len(values) <= 1:
		return values.copy()

	pivot = values[len(values) // 2]
	less = [value for value in values if value < pivot]
	equal = [value for value in values if value == pivot]
	greater = [value for value in values if value > pivot]

	return quick_sort(less) + equal + quick_sort(greater)


def bubble_sort(values: list[int]) -> list[int]:
	"""Return a sorted copy of values using the BubbleSort algorithm.

	Steps:
	1. Compare each pair of neighboring values.
	2. Swap a pair when the left value is larger than the right value.
	3. After one pass, the largest unsorted value has moved to the end.
	4. Repeat for the remaining unsorted section.

	BubbleSort is simpler than QuickSort, but it usually takes O(n**2) time.
	The early-exit check makes an already sorted list finish in O(n) time.
	Like QuickSort here, it returns a new list instead of changing the input.
	"""
	sorted_values = values.copy()

	for end_index in range(len(sorted_values) - 1, 0, -1):
		swapped = False
		for index in range(end_index):
			if sorted_values[index] > sorted_values[index + 1]:
				sorted_values[index], sorted_values[index + 1] = (
					sorted_values[index + 1],
					sorted_values[index],
				)
				swapped = True

		# Stop early when a complete pass makes no swaps.
		if not swapped:
			break

	return sorted_values


if __name__ == "__main__":
	numbers = [64, 34, 25, 12, 22, 11, 90, 25]
	print("Original:", numbers)
	print("QuickSort:", quick_sort(numbers))
	print("BubbleSort:", bubble_sort(numbers))
