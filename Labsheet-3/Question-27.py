# Program to find the second largest number in a list
elements = input("Enter integers separated by space: ").split()
lst = list(set([int(x) for x in elements]))

if len(lst) >= 2:
    lst.sort()
    print("Second largest number:", lst[-2])
else:
    print("List doesn't have enough unique elements.")