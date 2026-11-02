# Update a student's name using their ID

import sqlite3

try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()

    student_id = int(input("Enter student ID: "))
    new_name = input("Enter new name: ")

    cursor.execute("""
        UPDATE students
        SET name = ?
        WHERE id = ?
    """, (new_name, student_id))

    connection.commit()

    if cursor.rowcount > 0:
        print("Student name updated successfully!")
    else:
        print("Student ID not found.")

except ValueError:
    print("Enter a valid student ID.")
except sqlite3.Error as e:
    print("Database error:", e)

finally:
    if 'connection' in locals():
        connection.close()