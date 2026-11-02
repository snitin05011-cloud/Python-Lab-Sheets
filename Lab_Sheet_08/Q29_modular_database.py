# Use functions to insert and retrieve student records

import sqlite3

# Function to insert a student record
def insert_student(name, age, marks):
    connection = sqlite3.connect("student_db.db")

    try:
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO students (name, age, marks)
            VALUES (?, ?, ?)
        """, (name, age, marks))

        connection.commit()
        print("Student inserted successfully.")

    except sqlite3.Error as e:
        print("Database error:", e)

    finally:
        connection.close()


# Function to fetch and display student records
def fetch_students():
    connection = sqlite3.connect("student_db.db")

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students")

        records = cursor.fetchall()

        print("Student Records:")
        for record in records:
            print(record)

    except sqlite3.Error as e:
        print("Database error:", e)

    finally:
        connection.close()


# Main program
try:
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    marks = float(input("Enter student marks: "))

    insert_student(name, age, marks)
    fetch_students()

except ValueError:
    print("Please enter valid numeric values.")