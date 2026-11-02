# Retrieve and display all student records

import sqlite3

try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")

    records = cursor.fetchall()

    print("Student Records:")
    for record in records:
        print(record)

except sqlite3.Error as e:
    print("Database error:", e)

finally:
    if 'connection' in locals():
        connection.close()