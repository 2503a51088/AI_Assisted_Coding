def check_number(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Test with three different inputs
for value in [4, 7, 0]:
    print(value, ":", check_number(value))

# Decision: Accept
# Reason: The function correctly identifies even and odd numbers.
# Improvement: Use a clearer parameter name and add a docstring.