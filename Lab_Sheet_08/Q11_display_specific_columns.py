# Display only name and marks from the students table

import sqlite3

try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()

    cursor.execute("SELECT name, marks FROM students")

    records = cursor.fetchall()

    print("Name\t\tMarks")
    print("-----------------------")

    for record in records:
        print(f"{record[0]}\t\t{record[1]}")

except sqlite3.Error as e:
    print("Database error:", e)

finally:
    if 'connection' in locals():
        connection.close()