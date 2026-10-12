# Program to remove duplicates from a list using a set
elements = input("Enter elements of the list separated by space: ").split()
unique_list = list(set(elements))

print("List after removing duplicates:", unique_list)