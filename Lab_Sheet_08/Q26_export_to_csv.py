# Export all student records from SQLite to a CSV file

import sqlite3
import csv

try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    # Retrieve column names
    columns = [description[0] for description in cursor.description]

    with open("students_export.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(columns)
        writer.writerows(records)

    print("Student data exported to students_export.csv.")

except (sqlite3.Error, OSError) as e:
    print("Error:", e)

finally:
    if 'connection' in locals():
        connection.close()