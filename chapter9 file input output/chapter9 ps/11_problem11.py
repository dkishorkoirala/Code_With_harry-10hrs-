

with open("old.txt", "r") as f:
    content = f.read()

with open("renamed_by_python.txt", "w") as f:
    f.write(content)