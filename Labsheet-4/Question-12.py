# Program to find the maximum and minimum marks from a dictionary
n = int(input("Enter number of students: "))
students = {}

for _ in range(n):
    name = input("Enter student name: ")
    marks = float(input(f"Enter marks for {name}: "))
    students[name] = marks

if students:
    max_student = max(students, key=students.get)
    min_student = min(students, key=students.get)
    print(f"Highest marks: {students[max_student]} scored by {max_student}")
    print(f"Lowest marks: {students[min_student]} scored by {min_student}")
else:
    print("Dictionary is empty.")