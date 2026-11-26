def print_triangle_for(rows):
	for row in range(1, rows + 1):
		print("*" * row)


def print_triangle_while(rows):
	row = 1
	while row <= rows:
		print("*" * row)
		row += 1


print_triangle_for(5)
print_triangle_while(5)
