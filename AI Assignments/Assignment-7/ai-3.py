def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"File not found: {filename}"


print(read_file("nonexistent.txt"))
