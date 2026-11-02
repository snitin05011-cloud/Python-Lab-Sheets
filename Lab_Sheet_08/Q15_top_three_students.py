# Retrieve the top three students based on marks

import sqlite3

try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM students
        ORDER BY marks DESC
        LIMIT 3
    """)

    records = cursor.fetchall()

    print("Top 3 Students:")
    for record in records:
        print(record)

except sqlite3.Error as e:
    print("Database error:", e)

finally:
    if 'connection' in locals():
        connection.close()