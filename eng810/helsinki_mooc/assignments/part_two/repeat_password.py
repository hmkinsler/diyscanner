x = input("Password: ")

while True:
    y = input("Repeat password: ")
    if x != y:
        print("They do not match!")
    else:
        break

print("User account created!")