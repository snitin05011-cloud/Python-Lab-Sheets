# Program to remove duplicate elements from a list
elements = input("Enter elements separated by space: ").split()
unique_lst = []

for item in elements:
    if item not in unique_lst:
        unique_lst.append(item)

print("List after removing duplicates:", unique_lst)