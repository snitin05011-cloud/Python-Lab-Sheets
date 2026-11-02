# Q19: Sort words alphabetically and save them to a new file
try:
    with open("sample.txt", encoding="utf-8") as f:
        words = f.read().split()
    words.sort(key=str.lower)
    with open("sorted_words.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(words))
    print("Sorted words saved.")
except FileNotFoundError:
    print("Source file not found.")
except OSError as e:
    print("File error:", e)
