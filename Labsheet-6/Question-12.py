# Program to find the intersection of two sets
set1 = set(input("Enter elements for set 1 separated by space: ").split())
set2 = set(input("Enter elements for set 2 separated by space: ").split())

intersection_set = set1.intersection(set2)
print("Intersection of sets:", intersection_set)