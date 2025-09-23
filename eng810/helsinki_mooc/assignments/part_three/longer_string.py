x = input("Please type in string 1: ")
y = input("Please type in string 2: ")

if len(x) > len(y):
    print(f"{x} is longer")
elif len(y) > len(x):
    print(f"{y} is longer")
else:
    print("The strings are equally long")