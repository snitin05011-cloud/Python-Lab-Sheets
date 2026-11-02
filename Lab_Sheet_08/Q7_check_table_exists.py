# Check whether the students table exists

import sqlite3

try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type = 'table' AND name = ?
    """, ("students",))

    result = cursor.fetchone()

    if result:
        print("Students table exists.")
    else:
        print("Students table does not exist.")

except sqlite3.Error as e:
    print("Database error:", e)

finally:
    if 'connection' in locals():
        connection.close()