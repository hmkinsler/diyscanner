x = input("Please type in a string: ")
y = ""
z = y + x

while len(z) < 20:
    y += "*"
    z = y + x

print(z)