# Program to create a dictionary of student names and marks and display it
students = {}
n = int(input("Enter number of students: "))

for _ in range(n):
    name = input("Enter student name: ")
    marks = float(input(f"Enter marks for {name}: "))
    students[name] = marks

print("\n--- Student Marks Dictionary ---")
for name, marks in students.items():
    print(f"{name}: {marks}")