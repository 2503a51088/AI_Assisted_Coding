def check_discount(age, is_member):
	if age >= 60:
		if is_member:
			return "Senior discount and additional member discount"
		return "Senior discount"
	else:
		if is_member:
			return "Additional member discount"
		return "No discount"


if __name__ == "__main__":
	age = int(input("Enter your age: "))
	is_member = input("Are you a member? (yes/no): ").strip().lower() == "yes"
	print(check_discount(age, is_member))
