class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

# Create an instance of Student
student = Student(1, "John Doe")

# Add a new attribute student_class
student.student_class = "10th Grade"

# Display the entire attributes and their values
print("Attributes and their values before removing student_name:")
print(student.__dict__)

# Remove the student_name attribute
del student.student_name

# Display the entire attributes and their values after removal
print("\nAttributes and their values after removing student_name:")
print(student.__dict__)
