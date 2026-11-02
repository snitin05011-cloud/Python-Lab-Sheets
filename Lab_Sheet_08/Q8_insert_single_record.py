# Insert a single student record into the table

import sqlite3

try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()

    # Accept student details
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    marks = float(input("Enter student marks: "))

    # Insert data using parameterized query
    cursor.execute("""
        INSERT INTO students (name, age, marks)
        VALUES (?, ?, ?)
    """, (name, age, marks))

    connection.commit()
    print("Student record inserted successfully!")

except ValueError:
    print("Please enter valid numeric values.")
except sqlite3.Error as e:
    print("Database error:", e)

finally:
    if 'connection' in locals():
        connection.close()