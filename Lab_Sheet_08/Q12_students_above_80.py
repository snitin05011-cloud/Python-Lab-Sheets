# Display students who scored more than 80 marks

import sqlite3

try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM students
        WHERE marks > ?
    """, (80,))

    records = cursor.fetchall()

    print("Students scoring above 80:")
    for record in records:
        print(record)

except sqlite3.Error as e:
    print("Database error:", e)

finally:
    if 'connection' in locals():
        connection.close()