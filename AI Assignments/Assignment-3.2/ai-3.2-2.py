# Prompt 1: Sort the student marks.


def sort_marks_v1(marks):
	"""Initial vague version: sort marks in the default order."""
	return sorted(marks)


# Refined prompt:
# Sort student marks from highest to lowest. Accept only marks from 0 to 100.
# Reject any mark outside that range with a clear error message.
def sort_student_marks(marks):
	"""Sort valid student marks from highest to lowest.

	Validation takes O(n) time and sorting takes O(n log n) time.
	"""
	if any(mark < 0 or mark > 100 for mark in marks):
		return "Error: marks must be between 0 and 100"
	return sorted(marks, reverse=True)


if __name__ == "__main__":
	marks = [72, 95, 48, 88]

	print("Initial vague result:", sort_marks_v1(marks))
	print("Refined result:", sort_student_marks(marks))
	print("Constraint check:", sort_student_marks([105, 88, 76]))

	# Expected Output-2: the logic evolves from ambiguous to accurate sorting.
