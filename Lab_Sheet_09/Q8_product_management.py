# Store and manage product details using CRUD operations.

products = []

while True:
    print("\n--- Product Management ---")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            product_id = int(input("Enter product ID: "))

            if any(p["id"] == product_id for p in products):
                print("Product ID already exists.")
                continue

            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter quantity: "))

            products.append({
                "id": product_id,
                "name": name,
                "price": price,
                "quantity": quantity
            })

            print("Product added successfully!")

        elif choice == "2":
            if products:
                for product in products:
                    print(product)
            else:
                print("No products found.")

        elif choice == "3":
            product_id = int(input("Enter product ID to update: "))

            for product in products:
                if product["id"] == product_id:
                    product["price"] = float(input("Enter new price: "))
                    product["quantity"] = int(input("Enter new quantity: "))
                    print("Product updated successfully!")
                    break
            else:
                print("Product not found.")

        elif choice == "4":
            product_id = int(input("Enter product ID to delete: "))

            for product in products:
                if product["id"] == product_id:
                    products.remove(product)
                    print("Product deleted successfully!")
                    break
            else:
                print("Product not found.")

        elif choice == "5":
            print("Exiting application.")
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter valid numeric values.")