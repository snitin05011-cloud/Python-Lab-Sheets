# Create a new SQLite database

import sqlite3

try:
    # Create the database file if it does not exist
    connection = sqlite3.connect("student_db.db")

    print("Database student_db.db created successfully!")

except sqlite3.Error as e:
    print("Database error:", e)

finally:
    if 'connection' in locals():
        connection.close()