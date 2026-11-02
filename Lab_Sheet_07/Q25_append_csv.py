# Q25: Append a student record to an existing CSV file
import csv
try:
    name = input("Student name: ")
    age = int(input("Age: "))
    marks = float(input("Marks: "))
    with open("students.csv", "a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow([name, age, marks])
    print("Record appended.")
except ValueError:
    print("Enter valid numeric values for age and marks.")
except OSError as e:
    print("File error:", e)
