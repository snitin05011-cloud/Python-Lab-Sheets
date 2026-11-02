# Q27: Display selected Name and Marks columns from a CSV file
import csv
try:
    with open("students.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        print("Name\t\tMarks")
        print("-----------------------")
        for row in reader:
            print(f"{row['Name']}\t\t{row['Marks']}")
except FileNotFoundError:
    print("CSV file not found.")
except KeyError as e:
    print("Required column missing:", e)
except OSError as e:
    print("File error:", e)
