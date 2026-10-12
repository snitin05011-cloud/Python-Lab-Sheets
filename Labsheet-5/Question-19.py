# Program to remove duplicate elements from a tuple
elements = input("Enter elements separated by space: ").split()
my_tuple = tuple(elements)

# Converting to set to remove duplicates, then back to tuple
unique_tuple = tuple(dict.fromkeys(my_tuple))
print("Tuple after removing duplicates:", unique_tuple)