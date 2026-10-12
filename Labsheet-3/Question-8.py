# Q8_title_case.py
s = input("Enter a string: ")
res = ""
capitalize = True
for i in range(len(s)):
    ch = s[i]
    if ch == ' ':
        res += ch
        capitalize = True
    elif capitalize:
        if 'a' <= ch <= 'z':
            res += chr(ord(ch) - 32)
        else:
            res += ch
        capitalize = False
    else:
        if 'A' <= ch <= 'Z':
            res += chr(ord(ch) + 32)
        else:
            res += ch
print(f"Title case: {res}")