x = int(input("Please type in a number: "))

if x % 2 == 0:
    y = 0
    
    while y < x:
        y += 2
        print(y)
        print(y - 1)
        
        if y == x:
            break
elif x == 1:
    print(x)
else:
    y = 0 

    while y < x:
        y += 2
        print(y)
        print(y - 1)
        
        if (y + 1) >= x:
            break
    print(x)