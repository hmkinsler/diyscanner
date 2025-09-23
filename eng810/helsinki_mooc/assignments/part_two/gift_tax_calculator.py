x = int(input("Value of gift: "))

if x < 5000:
    print("No tax!")
if x >= 5000:
    if 5000 <= x < 25000:
        floor = 5000
        lower = 100
        rate = 0.08
        calc = lower + (x - floor) * rate
        print(f"""Amount of tax: {calc}""")
    elif 25000 <= x < 55000:
        floor = 25000
        lower = 1700
        rate = 0.10
        calc = lower + (x - floor) * rate
        print(f"""Amount of tax: {calc}""")
    elif 55000 <= x < 200000:
        floor = 55000
        lower = 4700
        rate = 0.12
        calc = lower + (x - floor) * rate
        print(f"""Amount of tax: {calc}""")
    elif 200000 <= x < 1000000:
        floor = 200000
        lower = 22100
        rate = 0.15
        calc = lower + (x - floor) * rate
        print(f"""Amount of tax: {calc}""")
    elif x >= 1000000:
        floor = 1000000
        lower = 142100
        rate = 0.17
        calc = lower + (x - floor) * rate
        print(f"""Amount of tax: {calc}""")