def factorial(number):  # Define a function to calculate factorial
    """Return the factorial of a non-negative integer."""  # Describe the function's purpose
    if number < 0:  # Factorial is not defined for negative numbers
        raise ValueError("Factorial is only defined for non-negative integers.")  # Stop for negative input

    result = 1  # Start with 1 because multiplying by 1 does not change the value
    for value in range(2, number + 1):  # Loop through numbers from 2 to the entered number
        result *= value  # Multiply the result by each value up to the entered number
    return result  # Return the calculated factorial


number = int(input("Enter a non-negative integer: "))  # Read and convert user input to an integer
print(f"The factorial of {number} is {factorial(number)}")  # Display the factorial result