# Perform CRUD operations on a list of books.

books = []

while True:
    print("\n--- Book Management System ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Update Book")
    print("4. Delete Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            book_id = int(input("Enter book ID: "))

            if any(book["id"] == book_id for book in books):
                print("Book ID already exists.")
                continue

            title = input("Enter book title: ")
            author = input("Enter author name: ")

            books.append({
                "id": book_id,
                "title": title,
                "author": author
            })

            print("Book added successfully!")

        elif choice == "2":
            if books:
                for book in books:
                    print(book)
            else:
                print("No books available.")

        elif choice == "3":
            book_id = int(input("Enter book ID to update: "))

            for book in books:
                if book["id"] == book_id:
                    book["title"] = input("Enter new title: ")
                    book["author"] = input("Enter new author: ")
                    print("Book updated successfully!")
                    break
            else:
                print("Book not found.")

        elif choice == "4":
            book_id = int(input("Enter book ID to delete: "))

            for book in books:
                if book["id"] == book_id:
                    books.remove(book)
                    print("Book deleted successfully!")
                    break
            else:
                print("Book not found.")

        elif choice == "5":
            print("Exiting application.")
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter valid numeric values.")