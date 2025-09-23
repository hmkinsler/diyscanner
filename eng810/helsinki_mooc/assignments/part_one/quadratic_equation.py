# Let's take the square root of math-module in use
from math import sqrt

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5
a = int(input("What is the value of variable a?"))
b = int(input("What is the value of variable b?"))
c = int(input("What is the value of variable c?"))

disc = sqrt((b ** 2) - (4 * a * c))

root_1 = ((b * -1) + disc) / (2 * a)
root_2 = ((b * -1) - disc) / (2 * a)

print(f"""The roots are {root_1} and {root_2}""")