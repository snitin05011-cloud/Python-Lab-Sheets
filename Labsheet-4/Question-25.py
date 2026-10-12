# Program to count word frequency in a given paragraph using a dictionary
paragraph = input("Enter a paragraph: ")
words = paragraph.lower().split()
word_freq = {}

for word in words:
    word = word.strip(".,!?;:\"'")
    if word:
        word_freq[word] = word_freq.get(word, 0) + 1

print("Word Frequencies:")
for word, count in word_freq.items():
    print(f"'{word}': {count}")