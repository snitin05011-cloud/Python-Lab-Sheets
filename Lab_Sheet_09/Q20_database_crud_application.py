# Menu-driven application for student CRUD operations using SQLite.

import sqlite3

DATABASE = "student_crud.db"

def create_table():
    # Create the students table if it does not exist.
    connection = None
    try:
        connection = sqlite3.connect(DATABASE)

        connection.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER,
                marks REAL
            )
        """)

        connection.commit()

    except sqlite3.Error as error:
        print("Database setup error:", error)

    finally:
        if connection:
            connection.close()


def add_student():
    # Insert a new student.
    connection = None
    try:
        roll = int(input("Enter roll number: "))
        name = input("Enter name: ").strip()
        age = int(input("Enter age: "))
        marks = float(input("Enter marks: "))

        if not name:
            raise ValueError("Name cannot be empty.")

        connection = sqlite3.connect(DATABASE)

        connection.execute("""
            INSERT INTO students (id, name, age, marks)
            VALUES (?, ?, ?, ?)
        """, (roll, name, age, marks))

        connection.commit()
        print("Student added successfully!")

    except ValueError as error:
        print("Invalid input:", error)

    except sqlite3.IntegrityError:
        print("Roll number already exists.")

    except sqlite3.Error as error:
        print("Database error:", error)

    finally:
        if connection:
            connection.close()


def view_students():
    # Display all student records.
    connection = None
    try:
        connection = sqlite3.connect(DATABASE)

        records = connection.execute(
            "SELECT * FROM students"
        ).fetchall()

        if records:
            print("\nStudent Records:")
            for record in records:
                print(record)
        else:
            print("No records found.")

    except sqlite3.Error as error:
        print("Database error:", error)

    finally:
        if connection:
            connection.close()


def update_student():
    # Update student marks using roll number.
    connection = None
    try:
        roll = int(input("Enter roll number: "))
        marks = float(input("Enter new marks: "))

        connection = sqlite3.connect(DATABASE)

        cursor = connection.execute(
            "UPDATE students SET marks = ? WHERE id = ?",
            (marks, roll)
        )

        connection.commit()

        if cursor.rowcount > 0:
            print("Student updated successfully!")
        else:
            print("Student not found.")

    except ValueError:
        print("Please enter valid numeric values.")

    except sqlite3.Error as error:
        print("Database error:", error)

    finally:
        if connection:
            connection.close()


def delete_student():
    # Delete a student using roll number.
    connection = None
    try:
        roll = int(input("Enter roll number to delete: "))

        connection = sqlite3.connect(DATABASE)

        cursor = connection.execute(
            "DELETE FROM students WHERE id = ?",
            (roll,)
        )

        connection.commit()

        if cursor.rowcount > 0:
            print("Student deleted successfully!")
        else:
            print("Student not found.")

    except ValueError:
        print("Please enter a valid roll number.")

    except sqlite3.Error as error:
        print("Database error:", error)

    finally:
        if connection:
            connection.close()


# Main program.
def main():
    create_table()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
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
            print("Exiting application. Thank you!")
            break

        else:
            print("Invalid choice. Please select 1 to 5.")


if __name__ == "__main__":
    main()