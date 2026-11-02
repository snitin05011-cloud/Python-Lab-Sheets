# Q14: Display the longest line in a file
try:
    with open("sample.txt", encoding="utf-8") as f:
        lines = f.readlines()
    if lines:
        longest = max(lines, key=len)
        print("Longest line:", longest, end="")
        print("Length:", len(longest.rstrip("\n")))
    else:
        print("File is empty.")
except FileNotFoundError:
    print("File not found.")
except OSError as e:
    print("File error:", e)
