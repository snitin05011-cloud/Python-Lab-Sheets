# Q12: Count occurrences of a whole word in a file
import re
try:
    with open("sample.txt", encoding="utf-8") as f:
        content = f.read()
    word = input("Enter word to count: ")
    matches = re.findall(r"\b" + re.escape(word) + r"\b", content, re.IGNORECASE)
    print(f"'{word}' occurs {len(matches)} time(s).")
except FileNotFoundError:
    print("File not found.")
except OSError as e:
    print("File error:", e)
