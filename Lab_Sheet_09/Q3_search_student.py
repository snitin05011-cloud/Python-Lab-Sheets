# Search for a student using their name.

students = [
    {"roll": 101, "name": "Aman", "age": 20, "marks": 85},
    {"roll": 102, "name": "Priya", "age": 21, "marks": 92},
    {"roll": 103, "name": "Rahul", "age": 20, "marks": 78}
]

search_name = input("Enter student name to search: ").strip()

# Search without considering uppercase/lowercase differences.
found = False

for student in students:
    if student["name"].lower() == search_name.lower():
        print("\nStudent found!")
        print(student)
        found = True
        break

if not found:
    print("Student not found.")