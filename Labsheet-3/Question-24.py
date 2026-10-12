# Program to reverse a list without using built-in functions
elements = input("Enter elements separated by space: ").split()
reversed_lst = []

for i in range(len(elements) - 1, -1, -1):
    reversed_lst.append(elements[i])

print("Reversed list:", reversed_lst)