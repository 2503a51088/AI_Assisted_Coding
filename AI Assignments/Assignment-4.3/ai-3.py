def format_name(full_name: str) -> str:
	"""Format a full name as 'Last, First Middle' when applicable."""
	if not isinstance(full_name, str):
		raise TypeError("full_name must be a string")

	name_parts = full_name.split()
	if len(name_parts) < 2:
		raise ValueError("enter at least a first name and a last name")

	first_name = " ".join(name_parts[:-1])
	last_name = name_parts[-1]
	return f"{last_name}, {first_name}"


if __name__ == "__main__":
	try:
		full_name = input("Enter your full name: ")
		print(format_name(full_name))
	except (TypeError, ValueError) as error:
		print(f"Error: {error}")
