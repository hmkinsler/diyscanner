while True:
    num = int(input("Please type in a number: "))
    x = 1
    y = 1

    if num >= 1:
        while x <= num:
            y *= x
            x += 1
        print(f"The factorial of the number {num} is {y}")

    else:
        break