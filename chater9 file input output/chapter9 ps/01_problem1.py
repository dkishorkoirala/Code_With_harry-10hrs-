f = open ("poem.txt")
content = f.read()
if ("twinkle" in content.lower()):
    print("Twinkle is present in the content")
else:
    print("Twinkle is not present in the content")

f.close()