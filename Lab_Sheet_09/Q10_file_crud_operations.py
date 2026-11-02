# Perform Create, Read, Update, and Delete operations on a file.

FILENAME = "student_records.txt"

def read_records():
    # Read all records from the file.
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            return [line.strip().split(",", 2) for line in file if line.strip()]
    except FileNotFoundError:
        return []

def save_records(records):
    # Save the updated records into the file.
    with open(FILENAME, "w", encoding="utf-8") as file:
        for record in records:
            file.write(",".join(record) + "\n")

while True:
    print("\n--- File CRUD Operations ---")
    print("1. Add Record")
    print("2. View Records")
    print("3. Modify Record")
    print("4. Delete Record")
    print("5. Exit")

    choice = input("Enter your choice: ")

    try:
        records = read_records()

        if choice == "1":
            roll = input("Enter roll number: ")

            if any(record[0] == roll for record in records):
                print("Roll number already exists.")
                continue

            name = input("Enter name: ")
            marks = input("Enter marks: ")

            records.append([roll, name, marks])
            save_records(records)
            print("Record added successfully!")

        elif choice == "2":
            if records:
                for record in records:
                    print(record)
            else:
                print("No records found.")

        elif choice == "3":
            roll = input("Enter roll number to modify: ")
            found = False

            for record in records:
                if record[0] == roll:
                    record[1] = input("Enter new name: ")
                    record[2] = input("Enter new marks: ")
                    found = True
                    break

            if found:
                save_records(records)
                print("Record updated successfully!")
            else:
                print("Record not found.")

        elif choice == "4":
            roll = input("Enter roll number to delete: ")
            updated = [record for record in records if record[0] != roll]

            if len(updated) < len(records):
                save_records(updated)
                print("Record deleted successfully!")
            else:
                print("Record not found.")

        elif choice == "5":
            print("Exiting application.")
            break

        else:
            print("Invalid choice.")

    except (OSError, ValueError) as error:
        print("Operation failed:", error)