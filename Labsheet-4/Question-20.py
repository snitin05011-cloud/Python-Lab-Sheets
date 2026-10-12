# Program to find the sum of all values in a dictionary
n = int(input("Enter number of elements: "))
d = {}
for _ in range(n):
    k = input("Enter key: ")
    v = float(input(f"Enter numeric value for '{k}': "))
    d[k] = v

total_sum = 0
for v in d.values():
    total_sum += v

print("Sum of all values:", total_sum)