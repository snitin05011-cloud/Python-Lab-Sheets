# Q6_char_frequency.py
s = input("Enter a string: ")
freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1
print("Character frequencies:")
for char, count in freq.items():
    print(f"'{char}': {count}")