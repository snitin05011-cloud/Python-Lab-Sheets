# Connect Python to an SQLite database

import sqlite3

try:
    # Connect to the database (creates it if it does not exist)
    connection = sqlite3.connect("student_db.db")

    print("Database connected successfully!")

except sqlite3.Error as e:
    print("Database error:", e)

finally:
    # Close the database connection
    if 'connection' in locals():
        connection.close()