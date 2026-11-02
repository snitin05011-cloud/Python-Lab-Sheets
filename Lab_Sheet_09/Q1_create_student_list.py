# Create a list of student records.

students = []

try:
    n = int(input("Enter the number of students: "))

    for i in range(n):
        print(f"\nEnter details of student {i + 1}:")
        roll = int(input("Roll Number: "))
        name = input("Name: ")
        age = int(input("Age: "))
        marks = float(input("Marks: "))

        # Store each student's details in a dictionary.
        student = {
            "roll": roll,
            "name": name,
            "age": age,
            "marks": marks
        }

        students.append(student)

    print("\nStudent records created successfully!")

    for student in students:
        print(student)

except ValueError:
    print("Invalid input! Please enter valid numeric values.")