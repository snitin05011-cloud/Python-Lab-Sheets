# Program to create a dictionary from a string with characters as keys and frequency as values
string = input("Enter a string: ")
char_freq = {}

for char in string:
    char_freq[char] = char_freq.get(char, 0) + 1

print("Character frequency dictionary:", char_freq)