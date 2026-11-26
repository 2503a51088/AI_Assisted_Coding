number1 = float(input("Enter the first number: "))  # Read the first number from the user
number2 = float(input("Enter the second number: "))  # Read the second number from the user

print("Choose an operation: +, -, *, /")  # Show available operations
operation = input("Enter operation: ")  # Read the chosen operation

if operation == "+":  # Check for addition
    result = number1 + number2  # Add the two numbers
elif operation == "-":  # Check for subtraction
    result = number1 - number2  # Subtract the second number from the first
elif operation == "*":  # Check for multiplication
    result = number1 * number2  # Multiply the two numbers
elif operation == "/":  # Check for division
    if number2 != 0:  # Prevent division by zero
        result = number1 / number2  # Divide the first number by the second
    else:
        result = "Error: Cannot divide by zero"  # Display an invalid-operation message
else:
    result = "Error: Invalid operation"  # Handle an unsupported operation

print("Result:", result)  # Display the final result5