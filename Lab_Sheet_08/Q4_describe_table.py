# Display the structure of the students table

import sqlite3

try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()

    # PRAGMA table_info displays column information
    cursor.execute("PRAGMA table_info(students)")

    columns = cursor.fetchall()

    print("Table Structure:")
    for column in columns:
        print(column)

except sqlite3.Error as e:
    print("Database error:", e)

finally:
    if 'connection' in locals():
        connection.close()