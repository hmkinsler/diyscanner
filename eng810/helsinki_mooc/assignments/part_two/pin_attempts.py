attempts = 0 
pin = 4321

while True:
    
    x = int(input("PIN: "))
    attempts += 1

    if x == 4321:
        success = True
        break

    print("Wrong")

if success == True and attempts == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"""Correct! It took you {attempts} attempts""")