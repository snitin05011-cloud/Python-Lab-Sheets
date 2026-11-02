# Find the student who scored the highest marks.

import sqlite3

connection = None

try:
    connection = sqlite3.connect("student_crud.db")

    record = connection.execute("""
        SELECT * FROM students
        WHERE marks = (SELECT MAX(marks) FROM students)
    """).fetchall()

    if record:
        print("Student(s) with the highest marks:")
        for student in record:
            print(student)
    else:
        print("No student records found.")

except sqlite3.Error as error:
    print("Database error:", error)

finally:
    if connection:
        connection.close()