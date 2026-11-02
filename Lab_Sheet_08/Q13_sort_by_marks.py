# Display students in descending order of marks

import sqlite3

try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM students
        ORDER BY marks DESC
    """)

    records = cursor.fetchall()

    print("Students sorted by marks:")
    for record in records:
        print(record)

except sqlite3.Error as e:
    print("Database error:", e)

finally:
    if 'connection' in locals():
        connection.close()