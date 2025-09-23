a = input("1st letter:")
b = input("2nd letter:")
c = input("3rd letter:")

if a > b > c:
    print(f"""The letter in the middle is {b}""")
elif c > b > a:
    print(f"""The letter in the middle is {b}""")
elif b > a > c:
    print(f"""The letter in the middle is {a}""")
elif c > a > b:
    print(f"""The letter in the middle is {a}""")
elif a > c > b:
    print(f"""The letter in the middle is {c}""")
elif b > c > a:
    print(f"""The letter in the middle is {c}""")
else:
    print("You are stuck.")