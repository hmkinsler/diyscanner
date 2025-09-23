num_1 = int(input("Please input number one:"))
num_2 = int(input("Please input number two:"))
oper = input("Please input the desired operation:")

if oper == "multiply":
    result = num_1 * num_2
    print(f"""{num_1} * {num_2} = {result}""")

if oper == "subtract":
    result = num_1 - num_2
    print(f"""{num_1} - {num_2} = {result}""")

if oper == "add":
    result = num_1 + num_2
    print(f"""{num_1} + {num_2} = {result}""")