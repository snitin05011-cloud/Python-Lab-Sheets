# Demonstrate handling of SQLite database errors

import sqlite3

try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()

    # Execute an invalid SQL statement to demonstrate error handling
    cursor.execute("SELECT * FROM invalid_table")

    records = cursor.fetchall()
    print(records)

except sqlite3.Error as e:
    print("SQLite database error occurred:")
    print(e)

finally:
    if 'connection' in locals():
        connection.close()