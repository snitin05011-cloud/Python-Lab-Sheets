# Save student records to a text file and read them.

try:
    n = int(input("Enter number of students: "))

    # Write student records into the file.
    with open("students.txt", "w", encoding="utf-8") as file:
        for i in range(n):
            print(f"\nStudent {i + 1}")
            roll = input("Enter roll number: ")
            name = input("Enter name: ")
            marks = input("Enter marks: ")

            file.write(f"{roll},{name},{marks}\n")

    print("\nStudent data saved successfully!")

    # Read and display the saved records.
    print("\nStudent Records:")

    with open("students.txt", "r", encoding="utf-8") as file:
        for line in file:
            roll, name, marks = line.strip().split(",", 2)
            print(f"Roll: {roll}, Name: {name}, Marks: {marks}")

except ValueError:
    print("Invalid number of students.")
except OSError as error:
    print("File error:", error)