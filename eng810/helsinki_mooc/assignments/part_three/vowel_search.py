string = input("Please type in a string: ")
vowels = ["a", "e", "o"]

for x in vowels:
    if x in string:
        print(x + " found")
    else: 
        print (x + " not found")