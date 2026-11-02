# Update marks of a student using their ID

import sqlite3

try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()

    student_id = int(input("Enter student ID: "))
    new_marks = float(input("Enter new marks: "))

    cursor.execute("""
        UPDATE students
        SET marks = ?
        WHERE id = ?
    """, (new_marks, student_id))

    connection.commit()

    if cursor.rowcount > 0:
        print("Student marks updated successfully!")
    else:
        print("Student ID not found.")

except ValueError:
    print("Enter valid numeric values.")
except sqlite3.Error as e:
    print("Database error:", e)

finally:
    if 'connection' in locals():
        connection.close()