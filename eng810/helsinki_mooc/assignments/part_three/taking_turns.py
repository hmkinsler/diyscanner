x = int(input("Please type in a number: "))
y = 1

# even numbers
if x % 2 == 0:
    while y <= x:
        print(y)
        print(x)
        y += 1
        x -= 1
# number equals 1
elif x == 1:
    print(x)
# odd numbers
else:
    while y <= x:
        print(y)
        print(x)
        y += 1
        x -= 1 

        if y == x:
            break
    print(y)
