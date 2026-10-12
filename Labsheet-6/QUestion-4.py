# Program to add multiple elements to a set using update()
my_set = {1, 2, 3}
print("Original set:", my_set)
elements = input("Enter multiple elements separated by space to add: ").split()
my_set.update(elements)

print("Set after update:", my_set)