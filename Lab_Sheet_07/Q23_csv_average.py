# Q23: Calculate averages of numeric columns in a CSV file
import csv
try:
    with open("students.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        ages, marks = [], []
        for row in reader:
            ages.append(float(row["Age"]))
            marks.append(float(row["Marks"]))
    if ages:
        print("Average Age:", sum(ages) / len(ages))
        print("Average Marks:", sum(marks) / len(marks))
    else:
        print("No records found.")
except FileNotFoundError:
    print("CSV file not found.")
except (ValueError, KeyError) as e:
    print("Invalid CSV data:", e)
except OSError as e:
    print("File error:", e)
