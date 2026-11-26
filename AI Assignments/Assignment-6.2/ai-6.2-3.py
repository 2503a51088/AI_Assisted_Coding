def check_number(number):
	if number > 0:
		return "positive"
	elif number < 0:
		return "negative"
	else:
		return "zero"


for number in (10, -5, 0):
	print(f"{number} is {check_number(number)}")
