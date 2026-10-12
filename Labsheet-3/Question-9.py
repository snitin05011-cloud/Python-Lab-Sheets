# Program to count the number of words in a string
string = input("Enter a string: ").strip()
if not string:
    count = 0
else:
    count = 1
    for char in string:
        if char == " ":
            count += 1

print(f"Number of words: {count}")