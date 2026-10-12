# Program to count the frequency of characters in a string using a dictionary
string = input("Enter a string: ")
freq = {}

for char in string:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print("Character Frequencies:")
for char, count in freq.items():
    print(f"'{char}': {count}")