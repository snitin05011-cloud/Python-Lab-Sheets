# Q3: Read a file line by line
try:
    with open("sample.txt", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
except FileNotFoundError:
    print("File not found.")
except OSError as e:
    print("File error:", e)
