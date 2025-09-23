x = input("Please type in a string: ")
y = len(x) - 1

while y >= 0:
    print(x[y:])
    y -= 1