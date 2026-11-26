from pathlib import Path


def count_lines(file_path: str) -> int:
	"""Return the number of lines in a .txt file.

	Few-shot behavior examples:
	- A file containing three text lines returns 3.
	- An empty text file returns 0.
	"""
	path = Path(file_path)
	if path.suffix.lower() != ".txt":
		raise ValueError("file must have a .txt extension")

	with path.open("r", encoding="utf-8") as text_file:
		return sum(1 for _line in text_file)


if __name__ == "__main__":
	file_name = input("Enter the path to a .txt file: ").strip()
	try:
		print(f"Line count: {count_lines(file_name)}")
	except (OSError, ValueError) as error:
		print(f"Error: {error}")
