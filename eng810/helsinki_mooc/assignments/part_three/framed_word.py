x = input("Word: ")

line = "******************************"
spaces = 28 - len(x)
l = spaces // 2
r = spaces - l

word = "*" + (l * " ") + x + (r * " ") + "*"

print(line)
print(word)
print(line)