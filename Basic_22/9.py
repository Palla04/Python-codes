import os

FILE_NAME = "students.txt"

# Function to add a student record
def add_student():
    name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")
    course = input("Enter course: ")

    # Save the record to a file
    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{roll_number},{course}\n")
    print("Student record added successfully.\n")

# Function to view all student records
def view_students():
    if not os.path.exists(FILE_NAME):
        print("No records found.\n")
        return

    with open(FILE_NAME, "r") as file:
        students = file.readlines()
        if not students:
            print("No records found.\n")
            return
        
        print("Student Records:")
        for student in students:
            name, roll_number, course = student.strip().split(",")
            print(f"Name: {name}, Roll Number: {roll_number}, Course: {course}")
    # print()

# Function to search for a student record by roll number
def search_student():
    roll_number = input("Enter roll number to search: ")
    found = False

    with open(FILE_NAME, "r") as file:
        for student in file:
            name, roll_no, course = student.strip().split(",")
            if roll_no == roll_number:
                print(f"Student found: Name: {name}, Roll Number: {roll_no}, Course: {course}\n")
                found = True
                break

    if not found:
        print("Student record not found.\n")

# Function to delete a student record by roll number
def delete_student():
    roll_number = input("Enter roll number to delete: ")
    found = False

    with open(FILE_NAME, "r") as file:
        students = file.readlines()

    with open(FILE_NAME, "w") as file:
        for student in students:
            name, roll_no, course = student.strip().split(",")
            if roll_no != roll_number:
                file.write(student)
            else:
                found = True

    if found:
        print("Student record deleted successfully.\n")
    else:
        print("Student record not found.\n")

# Main menu function
# def menu():
while True:
        print("Student Registry System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")

# Start the program
# if __name__ == "__main__":
#     menu()
