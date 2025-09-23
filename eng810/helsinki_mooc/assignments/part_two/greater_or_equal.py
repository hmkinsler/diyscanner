int1 = int(input("Please type in the first number: "))
int2 = int(input("Please type in another number: "))

if int1 > int2:
    print(f"""The greater number was: {int1}""")
elif int1 < int2:
    print(f"""The greater number was: {int2}""")
elif int1 == int2:
    print("The numbers are equal!")