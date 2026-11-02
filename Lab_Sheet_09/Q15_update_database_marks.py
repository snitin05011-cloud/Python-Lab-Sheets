# Update the marks of a student using roll number.

import sqlite3

connection = None

try:
    roll = int(input("Enter roll number: "))
    marks = float(input("Enter updated marks: "))

    connection = sqlite3.connect("student_crud.db")

    cursor = connection.execute(
        "UPDATE students SET marks = ? WHERE id = ?",
        (marks, roll)
    )

    connection.commit()

    if cursor.rowcount > 0:
        print("Student marks updated successfully!")
    else:
        print("Student not found.")

except ValueError:
    print("Please enter valid numeric values.")

except sqlite3.Error as error:
    print("Database error:", error)

finally:
    if connection:
        connection.close()