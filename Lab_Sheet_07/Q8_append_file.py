# Q8: Append content to an existing file
try:
    with open("sample.txt", "a", encoding="utf-8") as f:
        f.write("\n" + input("Enter content to append: "))
    print("Content appended.")
except OSError as e:
    print("File error:", e)
