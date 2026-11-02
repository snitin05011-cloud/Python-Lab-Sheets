# Q11: Search for a whole word in a file
import re
try:
    with open("sample.txt", encoding="utf-8") as f:
        content = f.read()
    word = input("Enter word to search: ")
    pattern = r"\b" + re.escape(word) + r"\b"
    print("Word found." if re.search(pattern, content, re.IGNORECASE) else "Word not found.")
except FileNotFoundError:
    print("File not found.")
except OSError as e:
    print("File error:", e)
