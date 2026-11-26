# Count positive, negative, and zero values in a list.

numbers = [10, -5, 0, 8, -2, 0]

positive_count = 0
negative_count = 0
zero_count = 0

# Loop and conditional logic suggested by an AI coding assistant
for number in numbers:
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
    else:
        zero_count += 1

# The AI suggestion was compared with my logic and used because it
# correctly handles positive numbers, negative numbers, and zero.
print("Positive:", positive_count)
print("Negative:", negative_count)
print("Zero:", zero_count)