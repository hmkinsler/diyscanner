wage = float(input("Hourly wage:"))
hours = int(input("Hours worked:"))
day = input("Day of the week:")

if day == "Sunday":
    wage = wage * 2

result = wage * hours

print(f"""Daily wages: {result} euros""")