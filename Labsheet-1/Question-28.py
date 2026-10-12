# Q28_char_type.py
ch = input("Enter a character: ")
if len(ch) == 1:
    if ch.isupper():
        print(f"'{ch}' is Uppercase.")
    elif ch.islower():
        print(f"'{ch}' is Lowercase.")
    elif ch.isdigit():
        print(f"'{ch}' is a Digit.")
    else:
        print(f"'{ch}' is a Special Character.")
else:
    print("Please enter exactly one character.")