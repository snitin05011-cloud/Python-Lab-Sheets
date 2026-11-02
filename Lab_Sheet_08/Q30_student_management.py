# Menu-driven application for student management
# Operations: Add, View, Update and Delete students

import sqlite3

# Function to create the students table
def create_table():
    connection = sqlite3.connect("student_db.db")

    try:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                marks REAL
            )
        """)

        connection.commit()

    except sqlite3.Error as e:
        print("Database error:", e)

    finally:
        connection.close()


# Function to add a student
def add_student():
    try:
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        marks = float(input("Enter student marks: "))

        connection = sqlite3.connect("student_db.db")
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO students (name, age, marks)
            VALUES (?, ?, ?)
        """, (name, age, marks))

        connection.commit()
        print("Student added successfully!")

    except ValueError:
        print("Enter valid numeric values.")

    except sqlite3.Error as e:
        print("Database error:", e)

    finally:
        if 'connection' in locals():
            connection.close()


# Function to view all students
def view_students():
    connection = sqlite3.connect("student_db.db")

    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students")

        records = cursor.fetchall()

        if records:
            print("\nID\tName\t\tAge\tMarks")
            print("----------------------------------------")

            for record in records:
                print(record)

        else:
            print("No student records found.")

    except sqlite3.Error as e:
        print("Database error:", e)

    finally:
        connection.close()


# Function to update student marks
def update_student():
    try:
        student_id = int(input("Enter student ID: "))
        new_marks = float(input("Enter new marks: "))

        connection = sqlite3.connect("student_db.db")
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE students
            SET marks = ?
            WHERE id = ?
        """, (new_marks, student_id))

        connection.commit()

        if cursor.rowcount > 0:
            print("Student updated successfully!")
        else:
            print("Student ID not found.")

    except ValueError:
        print("Enter valid numeric values.")

    except sqlite3.Error as e:
        print("Database error:", e)

    finally:
        if 'connection' in locals():
            connection.close()


# Function to delete a student
def delete_student():
    try:
        student_id = int(input("Enter student ID to delete: "))

        connection = sqlite3.connect("student_db.db")
        cursor = connection.cursor()

        cursor.execute("""
            DELETE FROM students
            WHERE id = ?
        """, (student_id,))

        connection.commit()

        if cursor.rowcount > 0:
            print("Student deleted successfully!")
        else:
            print("Student ID not found.")

    except ValueError:
        print("Enter a valid student ID.")

    except sqlite3.Error as e:
        print("Database error:", e)

    finally:
        if 'connection' in locals():
            connection.close()


# Main menu
create_table()

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student Marks")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Exiting Student Management System.")
        break

    else:
        print("Invalid choice. Please try again.")