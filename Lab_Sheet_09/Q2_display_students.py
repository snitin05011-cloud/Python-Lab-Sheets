# Display all student records from a list.

students = [
    {"roll": 101, "name": "Aman", "age": 20, "marks": 85},
    {"roll": 102, "name": "Priya", "age": 21, "marks": 92},
    {"roll": 103, "name": "Rahul", "age": 20, "marks": 78}
]

# Check whether the list contains records.
if students:
    print("Student Records:")

    for student in students:
        print(
            f"Roll: {student['roll']}, "
            f"Name: {student['name']}, "
            f"Age: {student['age']}, "
            f"Marks: {student['marks']}"
        )
else:
    print("No student records found.")