x = int(input("Width: "))
y = int(input("Height: "))
z = ""
a = 0

while a < y:
    while len(z) < x:
        z += "#"

    print(z)
    a += 1