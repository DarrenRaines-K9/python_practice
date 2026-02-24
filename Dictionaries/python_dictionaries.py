# Initialize an empty phonebook
phonebook = {}

# Function to add a contact
def add_contact(name, number):
    phonebook[name] = number
    print(f"Contact '{name}' added with number {number}.")

# Function to remove a contact
def remove_contact(name):
    if name in phonebook:
        del phonebook[name]
        print(f"Contact '{name}' removed.")
    else:
        print(f"Contact '{name}' not found.")

# Function to display all contacts
def display_contacts():
    print("Phonebook:")
    for name, number in phonebook.items():
        print(f"{name}: {number}")

# Adding contacts
add_contact("Alice", "123-456-7890")
add_contact("Bob", "987-654-3210")
add_contact("Charlie", "555-555-5555")

# Displaying contacts
display_contacts()

# Removing a contact
remove_contact("Bob")

# Displaying contacts again
display_contacts()

# View the entire dictionary
print(phonebook)

# Initialize an empty dictionary of student grades
student_grades = {}

# Function to add a student and grade
def add_student(name, grade):
    student_grades[name] = grade
    print(f"Student '{name}' added with grade {grade}.")    

# Function to remove a student
def remove_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"Student '{name}' removed.")
    else:
        print(f"Student '{name}' not found.")

# Function to display all students and their grades
def display_students():
    print("Student Grades:")
    for name, grade in student_grades.items():
        print(f"{name}: {grade}")

# Function to update a student's grade
def update_grade(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"Student '{name}' updated with grade {grade}.")
    else:
        print(f"Student '{name}' not found.")

def find_grade(name):
    if name in student_grades:
        return student_grades[name]
    else:
        print(f"Student '{name}' not found.")
        return None

def calculate_average_grade():
    if student_grades:
        average = sum(student_grades.values()) / len(student_grades)
        print(f"Average grade: {average:.2f}")
    else:
        print("No students found to calculate average grade.")

# Add some students
add_student("Alice", 85)
add_student("Bob", 92)
add_student("Charlie", 78)

# Display students and their grades
display_students()
# Update a student's grade
update_grade("Alice", 90)
# Remove a student
remove_student("Bob")
# Display students and their grades again
display_students()  
