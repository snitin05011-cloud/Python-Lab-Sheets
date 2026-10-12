# Program to check if a list is sorted or not
elements = input("Enter elements separated by space: ").split()
try:
    lst = [float(x) for x in elements]
except ValueError:
    lst = elements

is_ascending = True
is_descending = True

for i in range(len(lst) - 1):
    if lst[i] > lst[i + 1]:
        is_ascending = False
    if lst[i] < lst[i + 1]:
        is_descending = False

if is_ascending:
    print("The list is sorted in ascending order.")
elif is_descending:
    print("The list is sorted in descending order.")
else:
    print("The list is not sorted.")