# Program to find the first non-repeated character in a string
string = input("Enter a string: ")
non_repeated = None

for char in string:
    if string.count(char) == 1:
        non_repeated = char
        break

if non_repeated:
    print(f"First non-repeated character: '{non_repeated}'")
else:
    print("No non-repeated character found.")