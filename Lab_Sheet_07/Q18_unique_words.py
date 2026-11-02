# Q18: Store unique words in another file, preserving first occurrence
try:
    with open("sample.txt", encoding="utf-8") as f:
        words = f.read().split()
    unique_words = list(dict.fromkeys(words))
    with open("unique_words.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(unique_words))
    print("Unique words saved.")
except FileNotFoundError:
    print("Source file not found.")
except OSError as e:
    print("File error:", e)
