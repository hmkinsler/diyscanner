from math import sqrt
# Write your solution here

while True:
    x = int(input("Please type in a number: "))
    if x < 0:
        print("Invalid number")
    elif x > 0:
        print(sqrt(x))
    else:
        break

print("Exiting...")