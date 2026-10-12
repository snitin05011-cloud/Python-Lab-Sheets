# Program to access tuple elements using indexing
elements = input("Enter elements separated by space: ").split()
my_tuple = tuple(elements)

if my_tuple:
    index = int(input(f"Enter index (0 to {len(my_tuple)-1}): "))
    try:
        print(f"Element at index {index}: {my_tuple[index]}")
    except IndexError:
        print("Error: Index out of range.")
else:
    print("The tuple is empty.")