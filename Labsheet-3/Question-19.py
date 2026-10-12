# Program to find the most repeated word in a string
string = input("Enter a string: ")
words = string.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

if word_count:
    most_repeated = max(word_count, key=word_count.get)
    print(f"Most repeated word: '{most_repeated}' (Count: {word_count[most_repeated]})")
else:
    print("No words found.")