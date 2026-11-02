# Q26: Copy data from one CSV file to another
import csv
try:
    with open("students.csv", newline="", encoding="utf-8") as source:
        data = list(csv.reader(source))
    with open("students_copy.csv", "w", newline="", encoding="utf-8") as destination:
        csv.writer(destination).writerows(data)
    print("CSV data copied.")
except FileNotFoundError:
    print("Source CSV file not found.")
except OSError as e:
    print("File error:", e)
