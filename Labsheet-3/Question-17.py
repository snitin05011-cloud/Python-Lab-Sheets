# Program to print all substrings of a string
string = input("Enter a string: ")
n = len(string)

print("All substrings:")
for i in range(n):
    for j in range(i + 1, n + 1):
        print(string[i:j])