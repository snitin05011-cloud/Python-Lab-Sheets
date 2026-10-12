# Program to create a nested dictionary for student details (Name, Roll, Marks)
students = {}
n = int(input("Enter number of students: "))

for i in range(1, n + 1):
    roll = input(f"Enter Roll Number for student {i}: ")
    name = input(f"Enter Name for student {i}: ")
    marks = float(input(f"Enter Marks for student {i}: "))
    
    students[roll] = {
        "Name": name,
        "Marks": marks
    }

print("\n--- Nested Student Dictionary ---")
for roll, details in students.items():
    print(f"Roll: {roll} -> Name: {details['Name']}, Marks: {details['Marks']}")