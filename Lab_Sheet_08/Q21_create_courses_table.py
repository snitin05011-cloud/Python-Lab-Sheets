# Create a courses table and insert course records

import sqlite3

try:
    connection = sqlite3.connect("student_db.db")
    cursor = connection.cursor()

    # Create the courses table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            course_id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_name TEXT NOT NULL
        )
    """)

    # Add course_id to students if it does not already exist
    cursor.execute("PRAGMA table_info(students)")
    columns = [column[1] for column in cursor.fetchall()]

    if "course_id" not in columns:
        cursor.execute("""
            ALTER TABLE students
            ADD COLUMN course_id INTEGER
        """)

    # Insert sample courses
    courses = [
        ("Python Programming",),
        ("Database Management",),
        ("Web Development",)
    ]

    cursor.executemany("""
        INSERT INTO courses (course_name)
        SELECT ?
        WHERE NOT EXISTS (
            SELECT 1 FROM courses WHERE course_name = ?
        )
    """, [(name[0], name[0]) for name in courses])

    connection.commit()

    print("Courses table created and course records inserted.")

except sqlite3.Error as e:
    print("Database error:", e)

finally:
    if 'connection' in locals():
        connection.close()