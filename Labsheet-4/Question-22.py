# Program to create a dictionary with numbers as keys and their squares as values
n = int(input("Enter the value of n: "))
squares_dict = {}

for i in range(1, n + 1):
    squares_dict[i] = i * i

print("Dictionary of numbers and their squares:", squares_dict)