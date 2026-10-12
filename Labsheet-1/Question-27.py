# Q27_vowel_consonant.py
ch = input("Enter a character: ").lower()
if len(ch) == 1 and ch.isalpha():
    if ch in 'aeiou':
        print(f"'{ch}' is a Vowel.")
    else:
        print(f"'{ch}' is a Consonant.")
else:
    print("Invalid input! Please enter a single alphabetic character.")