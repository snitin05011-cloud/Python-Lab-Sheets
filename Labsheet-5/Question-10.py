# Program to repeat a tuple n times
elements = input("Enter elements separated by space: ").split()
my_tuple = tuple(elements)
n = int(input("Enter the number of times to repeat: "))

repeated_tuple = my_tuple * n
print("Repeated Tuple:", repeated_tuple)