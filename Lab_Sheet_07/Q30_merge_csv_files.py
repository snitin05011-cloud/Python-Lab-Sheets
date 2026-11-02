# Q30: Combine multiple CSV files, retaining only the first header
import csv

input_files = ["students1.csv", "students2.csv"]
try:
    with open("combined_students.csv", "w", newline="", encoding="utf-8") as output:
        writer = csv.writer(output)
        for index, filename in enumerate(input_files):
            with open(filename, newline="", encoding="utf-8") as source:
                for row_number, row in enumerate(csv.reader(source)):
                    if index == 0 or row_number > 0:
                        writer.writerow(row)
    print("CSV files combined successfully.")
except FileNotFoundError as e:
    print("Input file not found:", e.filename)
except OSError as e:
    print("File error:", e)
