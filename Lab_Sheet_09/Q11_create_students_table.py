# Connect to SQLite and create the students table.

import sqlite3

connection = None

try:
    connection = sqlite3.connect("student_crud.db")

    connection.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            marks REAL
        )
    """)

    connection.commit()
    print("Students table created successfully!")

except sqlite3.Error as error:
    print("Database error:", error)

finally:
    if connection:
        connection.close()