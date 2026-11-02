# Search for a student using their roll number.

import sqlite3

connection = None

try:
    roll = int(input("Enter roll number to search: "))

    connection = sqlite3.connect("student_crud.db")

    record = connection.execute(
        "SELECT * FROM students WHERE id = ?",
        (roll,)
    ).fetchone()

    if record:
        print("\nStudent found!")
        print(record)
    else:
        print("Student not found.")

except ValueError:
    print("Please enter a valid roll number.")

except sqlite3.Error as error:
    print("Database error:", error)

finally:
    if connection:
        connection.close()