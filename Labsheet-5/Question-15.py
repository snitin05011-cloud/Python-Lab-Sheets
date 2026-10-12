# Program to sort a tuple of numbers in ascending order
elements = input("Enter numbers separated by space: ").split()
my_tuple = tuple(float(x) for x in elements)

sorted_tuple = tuple(sorted(my_tuple))
print("Sorted Tuple (Ascending):", sorted_tuple)