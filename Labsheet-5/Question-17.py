# Program to reverse a tuple
elements = input("Enter elements separated by space: ").split()
my_tuple = tuple(elements)

reversed_tuple = my_tuple[::-1]
print("Reversed Tuple:", reversed_tuple)