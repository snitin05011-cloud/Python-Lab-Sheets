# Program to find unique words in a sentence using a set
sentence = input("Enter a sentence: ")
words = sentence.split()
unique_words = set(words)

print("Unique words:", unique_words)