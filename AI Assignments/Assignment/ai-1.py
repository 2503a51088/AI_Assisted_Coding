# Calculate and display the total marks for five subjects.

subject_names = ["WTP", "OS/CS", "IMS", "CC", "AI"]
total_marks = 0

for subject_name in subject_names:
    marks = int(input(f"Enter marks for {subject_name}: "))
    total_marks += marks

print("Total Marks:", total_marks)