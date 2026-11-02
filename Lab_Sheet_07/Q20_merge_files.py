# Q20: Merge two text files into a third file
try:
    with open("file1.txt", encoding="utf-8") as f1:
        first = f1.read()
    with open("file2.txt", encoding="utf-8") as f2:
        second = f2.read()
    with open("merged.txt", "w", encoding="utf-8") as output:
        output.write(first)
        if first and not first.endswith("\n"):
            output.write("\n")
        output.write(second)
    print("Files merged into merged.txt.")
except FileNotFoundError as e:
    print("Input file not found:", e.filename)
except OSError as e:
    print("File error:", e)
