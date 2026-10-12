# Program to remove all negative numbers from a list
elements = input("Enter integers separated by space: ").split()
lst = [int(x) for x in elements]
positive_list = []

for num in lst:
    if num >= 0:
        positive_list.append(num)

print("List after removing negative numbers:", positive_list)