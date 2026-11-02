# Count the number of students belonging to each age group

import sqlite3

try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT age, COUNT(*)
        FROM students
        GROUP BY age
        ORDER BY age
    """)

    records = cursor.fetchall()

    print("Age\tNumber of Students")
    for age, count in records:
        print(age, "\t", count)

except sqlite3.Error as e:
    print("Database error:", e)

finally:
    if 'connection' in locals():
        connection.close()