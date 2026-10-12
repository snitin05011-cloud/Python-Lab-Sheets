# Program to find the length of the longest word in a tuple
words = tuple(input("Enter words separated by space: ").split())

if words:
    longest = max(words, key=len)
    print(f"The longest word is '{longest}' with length {len(longest)}.")
else:
    print("The tuple is empty.")