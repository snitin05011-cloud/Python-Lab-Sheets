# Import student records from a CSV file into SQLite

import sqlite3
import csv

try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()

    with open("students_import.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        # Read and prepare student records
        students = [
            (row["name"], int(row["age"]), float(row["marks"]))
            for row in reader
        ]

    # Insert all CSV records into the table
    cursor.executemany("""
        INSERT INTO students (name, age, marks)
        VALUES (?, ?, ?)
    """, students)

    connection.commit()

    print(len(students), "student record(s) imported successfully.")

except FileNotFoundError:
    print("students_import.csv not found.")
except (ValueError, KeyError) as e:
    print("Invalid CSV data:", e)
except (sqlite3.Error, OSError) as e:
    print("Error:", e)

finally:
    if 'connection' in locals():
        connection.close()