# Program to iterate through a set and print its elements
elements = input("Enter elements separated by space: ").split()
my_set = set(elements)

print("Iterating through the set:")
for item in my_set:
    print(item)