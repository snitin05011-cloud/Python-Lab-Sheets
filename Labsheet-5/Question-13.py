# Program to find the maximum and minimum values in a tuple
elements = input("Enter numeric elements separated by space: ").split()
my_tuple = tuple(float(x) for x in elements)

if my_tuple:
    print("Maximum value:", max(my_tuple))
    print("Minimum value:", min(my_tuple))
else:
    print("The tuple is empty.")