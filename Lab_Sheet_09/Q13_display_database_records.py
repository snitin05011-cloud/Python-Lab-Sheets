# Read and display all student records.

import sqlite3

connection = None

try:
    connection = sqlite3.connect("student_crud.db")

    cursor = connection.execute("SELECT * FROM students")
    records = cursor.fetchall()

    if records:
        print("\nStudent Records:")
        for record in records:
            print(record)
    else:
        print("No student records found.")

except sqlite3.Error as error:
    print("Database error:", error)

finally:
    if connection:
        connection.close()