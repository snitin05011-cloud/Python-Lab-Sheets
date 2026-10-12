# Program to find the longest word in a string
string = input("Enter a string: ")
words = string.split()
longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)