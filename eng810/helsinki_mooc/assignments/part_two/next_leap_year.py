year = int(input("Year: "))

x = year
y = x + 1

while True:
    leap = False
    next_leap = False

# Check to see if initial year provided is a leap year
    # Year is not divisible by 100 and is divisible by 4:
    if x % 100 != 0 and x % 4 == 0:
        leap = True
    # Year is divisible by 100 and 400:
    elif x % 100 == 0 and x % 4 == 0 and x % 400 == 0:
        leap = True
    else: 
        x += 1
    
# Check to identify next possible leap year
    # Year is not divisible by 100 and is divisible by 4:
    if y % 100 != 0 and y % 4 == 0:
        next_leap = True
     # Year is divisible by 100 and 400:
    elif y % 100 == 0 and y % 4 == 0 and y % 400 == 0:
        next_leap = True
    else:
        y += 1

    if leap == True:
        if next_leap == True:
            break
        else: 
            next_leap = False

print(f"""The next leap year after {year} is {y}""")