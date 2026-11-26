def quick_sort(values: list[int]) -> list[int]:
	"""Sort values with QuickSort and return a new list.

	QuickSort steps:
	1. Choose a pivot value from the list.
	2. Divide the other values into smaller and larger groups.
	3. Recursively sort both groups.
	4. Combine the sorted smaller group, pivot values, and larger group.

	The average time complexity is O(n log n); the worst case is O(n**2).
	"""
	if len(values) <= 1:
		return values.copy()

	# Choosing the middle item makes the example easy to follow.
	pivot = values[len(values) // 2]
	smaller = [value for value in values if value < pivot]
	equal = [value for value in values if value == pivot]
	larger = [value for value in values if value > pivot]

	return quick_sort(smaller) + equal + quick_sort(larger)


def bubble_sort(values: list[int]) -> list[int]:
	"""Sort values with BubbleSort and return a new list.

	BubbleSort steps:
	1. Compare each pair of neighboring values.
	2. Swap the pair when the left value is larger.
	3. One complete pass moves the largest unsorted value to the end.
	4. Repeat until a pass makes no swaps.

	BubbleSort is easier to understand but usually takes O(n**2) time.
	Its early-exit check takes O(n) time when the list is already sorted.
	"""
	sorted_values = values.copy()

	# Each pass handles one fewer item because the end is already sorted.
	for end_index in range(len(sorted_values) - 1, 0, -1):
		swapped = False
		for index in range(end_index):
			if sorted_values[index] > sorted_values[index + 1]:
				sorted_values[index], sorted_values[index + 1] = (
					sorted_values[index + 1],
					sorted_values[index],
				)
				swapped = True

		if not swapped:
			break

	return sorted_values


# Difference: QuickSort divides the list into partitions, while BubbleSort
# repeatedly compares neighboring items. QuickSort is generally faster for
# larger lists; BubbleSort is mainly useful for learning and small lists.
if __name__ == "__main__":
	numbers = [64, 34, 25, 12, 22, 11, 90, 25]
	print("Original:   ", numbers)
	print("QuickSort:  ", quick_sort(numbers))
	print("BubbleSort: ", bubble_sort(numbers))
