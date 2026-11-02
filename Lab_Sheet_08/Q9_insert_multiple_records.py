# Insert multiple student records using executemany()

import sqlite3

try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()

    # Sample student records
    students = [
        ("Aman", 20, 85),
        ("Rahul", 21, 90),
        ("Priya", 20, 95),
        ("Neha", 22, 78),
        ("Karan", 21, 65)
    ]

    # Insert all records together
    cursor.executemany("""
        INSERT INTO students (name, age, marks)
        VALUES (?, ?, ?)
    """, students)

    connection.commit()
    print("Multiple student records inserted successfully!")

except sqlite3.Error as e:
    print("Database error:", e)

finally:
    if 'connection' in locals():
        connection.close()