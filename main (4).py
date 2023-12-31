
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Example usage:
students1 = [
    Student("Alice", "A001", 3.8),
    Student("Bob", "B002", 3.5),
    Student("Charlie", "C003", 3.9),
    Student("David", "D004", 3.7)
]
sorted_students1 = sort_students(students1)

# Printing sorted students for both test cases
print("Sorted Students 1:")
for student in sorted_students1:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")