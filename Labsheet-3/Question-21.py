# Program to find the largest and smallest elements in a list
elements = input("Enter elements separated by space: ").split()
lst = [int(x) for x in elements]

if lst:
    print("Largest element:", max(lst))
    print("Smallest element:", min(lst))
else:
    print("List is empty.")