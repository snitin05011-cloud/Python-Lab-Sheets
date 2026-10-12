# Program to sort a tuple of strings alphabetically
elements = input("Enter strings separated by space: ").split()
my_tuple = tuple(elements)

sorted_tuple = tuple(sorted(my_tuple))
print("Sorted Tuple (Alphabetically):", sorted_tuple)