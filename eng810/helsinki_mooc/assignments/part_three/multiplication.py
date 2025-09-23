num = int(input("Please type in a number: "))

x = 1 
y = 1



while x <= num:
    print(f"{x} x {y} = {(x * y)}")
    while y < num:
        y += 1
        print(f"{x} x {y} = {(x * y)}")
    x += 1
    y = 1