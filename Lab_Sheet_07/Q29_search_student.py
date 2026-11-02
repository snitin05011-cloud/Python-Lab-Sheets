# Q29: Search for a student record by name
import csv
try:
    target = input("Enter student name to search: ").strip().lower()
    found = False
    with open("students.csv", newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["Name"].strip().lower() == target:
                print("Record found:", row)
                found = True
    if not found:
        print("Student record not found.")
except FileNotFoundError:
    print("CSV file not found.")
except KeyError as e:
    print("Required column missing:", e)
except OSError as e:
    print("File error:", e)
