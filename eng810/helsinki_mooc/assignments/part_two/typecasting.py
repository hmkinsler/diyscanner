number = float(input("Please type in a number: "))

integer = int(number)
decimal = abs(integer - number)

print(f"""Integer part: {integer}""")
print(f"""Decimal part: {decimal}""")