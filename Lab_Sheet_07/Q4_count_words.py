# Q4: Count the number of words in a text file
try:
    with open("sample.txt", encoding="utf-8") as f:
        words = f.read().split()
    print("Number of words:", len(words))
except FileNotFoundError:
    print("File not found.")
except OSError as e:
    print("File error:", e)
