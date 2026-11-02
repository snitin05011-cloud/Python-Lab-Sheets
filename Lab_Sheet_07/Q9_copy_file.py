# Q9: Copy contents from one text file to another
try:
    with open("sample.txt", encoding="utf-8") as source:
        content = source.read()
    with open("copy.txt", "w", encoding="utf-8") as destination:
        destination.write(content)
    print("File copied successfully.")
except FileNotFoundError:
    print("Source file not found.")
except OSError as e:
    print("File error:", e)
