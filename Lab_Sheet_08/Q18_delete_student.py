# Delete a student record using student ID

import sqlite3

try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()

    student_id = int(input("Enter student ID to delete: "))

    cursor.execute("""
        DELETE FROM students
        WHERE id = ?
    """, (student_id,))

    connection.commit()

    if cursor.rowcount > 0:
        print("Student record deleted successfully!")
    else:
        print("Student ID not found.")

except ValueError:
    print("Enter a valid student ID.")
except sqlite3.Error as e:
    print("Database error:", e)

finally:
    if 'connection' in locals():
        connection.close()