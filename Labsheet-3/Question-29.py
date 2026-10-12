# Program to find the difference between two lists
list1 = input("Enter elements for first list separated by space: ").split()
list2 = input("Enter elements for second list separated by space: ").split()
difference = []

for item in list1:
    if item not in list2 and item not in difference:
        difference.append(item)

print("Difference (list1 - list2):", difference)