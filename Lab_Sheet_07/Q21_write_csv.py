# Q21: Create a CSV file and write student records
import csv
try:
    with open("students.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age", "Marks"])
        writer.writerows([["Aman", 20, 85], ["Rahul", 21, 90], ["Priya", 20, 95]])
    print("CSV file created.")
except OSError as e:
    print("File error:", e)
