# Program to find the key with the maximum value in a dictionary
n = int(input("Enter number of elements: "))
d = {}
for _ in range(n):
    k = input("Enter key: ")
    v = float(input(f"Enter numeric value for '{k}': "))
    d[k] = v

if d:
    max_key = max(d, key=d.get)
    print(f"Key with maximum value: '{max_key}' with value {d[max_key]}")
else:
    print("Dictionary is empty.")