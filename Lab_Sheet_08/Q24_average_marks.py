# Calculate the average marks of all students

import sqlite3

try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()

    cursor.execute("SELECT AVG(marks) FROM students")

    average = cursor.fetchone()[0]

    if average is not None:
        print("Average marks:", round(average, 2))
    else:
        print("No student records found.")

except sqlite3.Error as e:
    print("Database error:", e)

finally:
    if 'connection' in locals():
        connection.close()