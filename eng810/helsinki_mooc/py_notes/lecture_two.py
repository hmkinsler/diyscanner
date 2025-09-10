# Last Week Review:

# 1. Kinds of statements
print("Hello, world!")

# 2. Inputting data
name = input("Enter your name: ")
print("Hello, " + name)

# 3. Variables

# 4. Reading integer type data
age = int(input("Enter your age: "))
print("You are ", age, "years old.")

# 5. Formatting output
    # Using f-strings
print(f"You are {age} years old.")

# 6. Simple conditional statements
year = int(input("Provide you birth year: "))

age = 2025 - year

if age >= 18:
    print("You are an adult.")

print("Thank you!")

# Programming terminology:
    # Statement: A statement is a part of the program which executes something. It often, but not always, refers to a single command.
    # Block: A block is a group of consecutive statements that are at the same level in the structure of the program.
    # Expression: An expression is a bit of code that results in a determined data type. When the program is executed, the expression is evaluated so that it has a value that can then be used in the program.
    # Function: A function executes some functionality. Functions can also take one or more arguments, which are data that can be fed to and processed by the function. 
    # Type: Data type refers to the characteristics of any value present in the program.
    # Syntax (semantics): Similarly to natural languages, the syntax of a programming language determines how the code of a program should be written.
    # Debugging: If the syntax of the program is correct but the program still doesn't function as intended, there is a bug in the program.

# More conditional statements:
    #  Optional branch with else statement
number = int(input("Provide a number:"))

if number < 0:
    number = -number
    print("This is a negative number")
    print("The absolute value of number is", number)
else:
    print("This is a positive number")
    print("The absolute value of number is", number)
   
    #  Optional branch with elif statement
number = int(input("Provide a number: "))

if number < 0:
    number = -number
    print("This is a negative number")
    print("The absolute value of number is", number)
elif number > 0:
    print("This is a positive number")
    print("The absolute value of number is", number)

    #Combining else and elif statements
animal = input("which animal?")

if animal == "dog":
    print("woof")
elif animal == "cat":
    print("meow")
elif animal == "cow":
    print("moo")
else:
        print("I don't know what that animal says")

    # Simplifying if statements
animal = input("which animal?")

if animal == "dog" or animal == "cat":
    print("That's a good pet")
    print("You can probably get one from the pet store")
elif animal == "lion" or animal == "elephant":
    print("That's probably not a good pet")
else:
    print("I don't know if that's a good pet")

# Logical operators
    #Example One
animal = input("which animal? ")
place = input("where do you live?")

if animal == "dog" or animal == "cat":
    print("That's a good pet")
    print("You can probably get one from the pet store")
elif animal == "lion" or animal == "elephant":
    print("That's probably not a good pet")
elif animal == "sheep" or animal == "cow" and place == "farm":
    print("You could probably get that animal")
else:
    print("I don't know if that's a good pet")

    # Example Two
age = int(input("What is your age? "))

if age >= 18 and age <40:
    print("You can enter!")
elif age < 18:
    print("You are not old enough to enter")
else:
    print("You are too old")

# Nested conditions
age = int(input("What is your age? "))

if age >= 18:
    print("You can enter")

    if age > 65:
        print("You get a senior discount!")
    else:
        print("Users over 65 will receive a senior discount")

else:
    print("You are too young to enter")

# Simple loop
while True:
    number = int(input("Give a number, 0 to stop: "))
   
    if number == 0:
        break

    print("The square of", number, "is", (number * number))

