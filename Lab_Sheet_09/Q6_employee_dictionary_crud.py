# Perform CRUD operations on employee data.

employees = {}

while True:
    print("\n--- Employee Management ---")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            emp_id = int(input("Enter employee ID: "))

            if emp_id in employees:
                print("Employee ID already exists.")
                continue

            name = input("Enter employee name: ")
            salary = float(input("Enter salary: "))

            employees[emp_id] = {
                "name": name,
                "salary": salary
            }

            print("Employee added successfully!")

        elif choice == "2":
            if employees:
                for emp_id, details in employees.items():
                    print(emp_id, details)
            else:
                print("No employee records found.")

        elif choice == "3":
            emp_id = int(input("Enter employee ID: "))

            if emp_id in employees:
                employees[emp_id]["salary"] = float(
                    input("Enter updated salary: ")
                )
                print("Employee updated successfully!")
            else:
                print("Employee not found.")

        elif choice == "4":
            emp_id = int(input("Enter employee ID: "))

            if emp_id in employees:
                del employees[emp_id]
                print("Employee deleted successfully!")
            else:
                print("Employee not found.")

        elif choice == "5":
            print("Exiting application.")
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Invalid input! Please enter correct values.")