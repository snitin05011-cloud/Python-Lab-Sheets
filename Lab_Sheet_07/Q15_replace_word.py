# Q15: Replace a word in a file with another word
try:
    with open("sample.txt", encoding="utf-8") as f:
        content = f.read()
    old = input("Word to replace: ")
    new = input("Replacement word: ")
    with open("sample.txt", "w", encoding="utf-8") as f:
        f.write(content.replace(old, new))
    print("Replacement completed.")
except FileNotFoundError:
    print("File not found.")
except OSError as e:
    print("File error:", e)
