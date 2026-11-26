#include <iostream>
#include <string>

class Student {
private:
    std::string name;
    int roll_number;
    double marks;

public:
    Student(const std::string& student_name, int student_roll_number, double student_marks)
        : name(student_name), roll_number(student_roll_number), marks(student_marks) {}

    void display() const {
        std::cout << "Student Details\n"
                  << "Name: " << name << '\n'
                  << "Roll Number: " << roll_number << '\n'
                  << "Marks: " << marks << '\n';
    }
};

int main() {
    const Student student("Alice", 101, 95.5);
    student.display();
    return 0;
}
