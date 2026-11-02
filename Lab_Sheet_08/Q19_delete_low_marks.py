# Delete students who scored less than 40 marks

import sqlite3

try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM students
        WHERE marks < ?
    """, (40,))

    connection.commit()

    print(cursor.rowcount, "student record(s) deleted.")

except sqlite3.Error as e:
    print("Database error:", e)

finally:
    if 'connection' in locals():
        connection.close()