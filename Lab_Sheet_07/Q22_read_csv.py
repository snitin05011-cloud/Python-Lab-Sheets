# Q22: Read and display data from a CSV file
import csv
try:
    with open("students.csv", newline="", encoding="utf-8") as f:
        for row in csv.reader(f):
            print(row)
except FileNotFoundError:
    print("CSV file not found. Run Q21 first.")
except OSError as e:
    print("File error:", e)
