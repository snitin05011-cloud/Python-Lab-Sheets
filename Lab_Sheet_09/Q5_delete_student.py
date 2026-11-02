# Delete a student record using roll number.

students = [
    {"roll": 101, "name": "Aman", "age": 20, "marks": 85},
    {"roll": 102, "name": "Priya", "age": 21, "marks": 92},
    {"roll": 103, "name": "Rahul", "age": 20, "marks": 78}
]

try:
    roll = int(input("Enter roll number to delete: "))

    found = False

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            print("Student record deleted successfully!")
            found = True
            break

    if not found:
        print("Student not found.")

    print("\nUpdated Student List:")
    for student in students:
        print(student)

except ValueError:
    print("Please enter a valid roll number.")