# Q24: Count data rows and columns in a CSV file (excluding header)
import csv
try:
    with open("students.csv", newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    if rows:
        print("Number of rows:", len(rows) - 1)
        print("Number of columns:", len(rows[0]))
    else:
        print("CSV file is empty.")
except FileNotFoundError:
    print("CSV file not found.")
except OSError as e:
    print("File error:", e)
