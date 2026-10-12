# Program to find pairs of numbers in a list whose sum is equal to a given number
elements = input("Enter integers separated by space: ").split()
lst = [int(x) for x in elements]
target = int(input("Enter the target sum: "))

print(f"Pairs with sum {target}:")
found = False
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == target:
            print(f"({lst[i]}, {lst[j]})")
            found = True

if not found:
    print("No such pairs found.")