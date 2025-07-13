try:
    with open("1.txt","r") as f:
        print(f.read())

except Exception as e:
    print("File not found")

try:
    with open("2.txt","r") as g:
        print(g.read())

except Exception as e:
    print("File not found")

try:
    with open("3.txt","r") as h:
        print(h.read())

except Exception as e:
    print("File not found")

print("Thank you")
