# Program to remove all elements of one set from another set (in-place difference update)
set1 = set(input("Enter elements for set 1: ").split())
set2 = set(input("Enter elements for set 2 to remove: ").split())

set1.difference_update(set2)
print("Set 1 after removing elements present in Set 2:", set1)