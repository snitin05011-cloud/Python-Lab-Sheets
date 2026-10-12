# Program to create a list of squares of numbers from 1 to n
n = int(input("Enter the value of n: "))
squares = []

for i in range(1, n + 1):
    squares.append(i * i)

print(f"List of squares from 1 to {n}:", squares)