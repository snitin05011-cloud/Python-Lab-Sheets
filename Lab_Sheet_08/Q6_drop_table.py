# Delete the students table from the database

import sqlite3

try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()

    # Drop the table if it exists
    cursor.execute("DROP TABLE IF EXISTS students")

    connection.commit()
    print("Students table dropped successfully!")

except sqlite3.Error as e:
    print("Database error:", e)

finally:
    if 'connection' in locals():
        connection.close()