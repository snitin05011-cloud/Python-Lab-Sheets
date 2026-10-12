# Program to convert a list into a tuple
elements = input("Enter list elements separated by space: ").split()
my_list = list(elements)

my_tuple = tuple(my_list)
print("Converted Tuple:", my_tuple)
print("Type:", type(my_tuple))