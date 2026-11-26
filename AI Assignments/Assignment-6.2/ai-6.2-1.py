class Student:
	def __init__(self, name, roll_no, marks):
		self.name = name
		self.roll_no = roll_no
		self.marks = marks

	def is_pass(self):
		return self.marks >= 40


student1 = Student("Anu", 1, 75)
student2 = Student("Ravi", 2, 35)

for student in (student1, student2):
	status = "passed" if student.is_pass() else "failed"
	print(f"{student.name} scored {student.marks} marks and {status}.")
