# Delete a student record using roll number.

import sqlite3

connection = None

try:
    roll = int(input("Enter roll number to delete: "))

    connection = sqlite3.connect("student_crud.db")

    cursor = connection.execute(
        "DELETE FROM students WHERE id = ?",
        (roll,)
    )

    connection.commit()

    if cursor.rowcount > 0:
        print("Student record deleted successfully!")
    else:
        print("Student not found.")

except ValueError:
    print("Please enter a valid roll number.")

except sqlite3.Error as error:
    print("Database error:", error)

finally:
    if connection:
        connection.close()