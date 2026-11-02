# Q28: Find the student with the highest marks
import csv
try:
    with open("students.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        best = max(reader, key=lambda row: float(row["Marks"]), default=None)
    if best:
        print("Name:", best["Name"])
        print("Highest Marks:", best["Marks"])
    else:
        print("No student records found.")
except FileNotFoundError:
    print("CSV file not found.")
except (ValueError, KeyError) as e:
    print("Invalid CSV data:", e)
except OSError as e:
    print("File error:", e)
