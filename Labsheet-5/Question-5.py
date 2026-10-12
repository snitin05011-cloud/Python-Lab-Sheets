# Program to access tuple elements using slicing
elements = input("Enter elements separated by space: ").split()
my_tuple = tuple(elements)

start = int(input("Enter start index: "))
end = int(input("Enter end index: "))

print("Sliced tuple:", my_tuple[start:end])