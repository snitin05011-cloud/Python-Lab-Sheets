# Display student records in alphabetical order of names.

import sqlite3

connection = None

try:
    connection = sqlite3.connect("student_crud.db")

    records = connection.execute("""
        SELECT * FROM students
        ORDER BY name ASC
    """).fetchall()

    if records:
        print("Students sorted by name:")
        for record in records:
            print(record)
    else:
        print("No student records found.")

except sqlite3.Error as error:
    print("Database error:", error)

finally:
    if connection:
        connection.close()