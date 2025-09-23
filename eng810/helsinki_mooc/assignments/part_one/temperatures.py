temp = int(input("Please type in a temperature (F):"))

conv = (temp - 32) * (5/9)

if conv >= 0:
    print(f"""{temp} degrees Fahrenheit equals {conv} degrees Celsius""")

if conv < 0:
    print(f"""{temp} degrees Fahrenheit equals {conv} degrees Celsius""")
    print("Brr! It's cold in here!")