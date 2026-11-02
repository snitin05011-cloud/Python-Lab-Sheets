# Delete all records while keeping the table structure

import sqlite3

try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()

    # SQLite does not support TRUNCATE TABLE.
    # DELETE FROM removes all records but preserves the table.
    cursor.execute("DELETE FROM students")

    connection.commit()

    print("All records deleted. Table structure is unchanged.")

except sqlite3.Error as e:
    print("Database error:", e)

finally:
    if 'connection' in locals():
        connection.close()