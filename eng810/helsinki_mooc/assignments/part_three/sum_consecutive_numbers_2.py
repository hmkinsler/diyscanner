x = int(input("Limit: "))
y = 1
sum = 1
sums = "1"

while sum < x :
    y += 1
    sum += y
    sums += f" + {y}"

print(f"The consecutive sum: {sums} = {sum}")