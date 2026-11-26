class Student:
    def __init__(self, name: str, roll_number: int, marks: float) -> None:
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display(self) -> None:
        print("Student Details")
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")


student = Student("Alice", 101, 95.5)
student.display()