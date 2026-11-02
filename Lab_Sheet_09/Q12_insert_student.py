# Insert a new student record into the database.

import sqlite3

connection = None

try:
    roll = int(input("Enter roll number: "))
    name = input("Enter student name: ").strip()
    age = int(input("Enter age: "))
    marks = float(input("Enter marks: "))

    if not name:
        raise ValueError("Name cannot be empty.")

    connection = sqlite3.connect("student_crud.db")

    connection.execute("""
        INSERT INTO students (id, name, age, marks)
        VALUES (?, ?, ?, ?)
    """, (roll, name, age, marks))

    connection.commit()
    print("Student record inserted successfully!")

except ValueError as error:
    print("Invalid input:", error)

except sqlite3.IntegrityError:
    print("A student with this roll number already exists.")

except sqlite3.Error as error:
    print("Database error:", error)

finally:
    if connection:
        connection.close()