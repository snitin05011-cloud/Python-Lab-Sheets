# Count the total number of student records.

import sqlite3

connection = None

try:
    connection = sqlite3.connect("student_crud.db")

    count = connection.execute(
        "SELECT COUNT(*) FROM students"
    ).fetchone()[0]

    print("Total number of student records:", count)

except sqlite3.Error as error:
    print("Database error:", error)

finally:
    if connection:
        connection.close()