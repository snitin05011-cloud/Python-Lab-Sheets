# Q5: Count the number of lines and characters in a file
try:
    with open("sample.txt", encoding="utf-8") as f:
        content = f.read()
    print("Number of lines:", len(content.splitlines()))
    print("Number of characters:", len(content))
except FileNotFoundError:
    print("File not found.")
except OSError as e:
    print("File error:", e)
