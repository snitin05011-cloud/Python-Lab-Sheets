# Display students along with their course names using INNER JOIN

import sqlite3

try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT students.name, students.marks, courses.course_name
        FROM students
        INNER JOIN courses
        ON students.course_id = courses.course_id
    """)

    records = cursor.fetchall()

    print("Student Name\tMarks\tCourse")
    for record in records:
        print(record)

except sqlite3.Error as e:
    print("Database error:", e)

finally:
    if 'connection' in locals():
        connection.close()