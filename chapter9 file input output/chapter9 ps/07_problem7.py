
# line = 1
with open("log.txt", "r") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if ("python" in line):
        print(f"Yes python is present. line number: {lineno}")
        break
    lineno += 1
else:
        print("No python is not present")