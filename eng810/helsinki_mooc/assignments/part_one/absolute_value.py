num = int(input("Please type in a number:"))

if num < 0:
   new_num = (num * -1)
   print(f"""The absolute value of this number is {new_num}""")

if num >= 0:
    print(f"""The absolute value of this number is {num}""")