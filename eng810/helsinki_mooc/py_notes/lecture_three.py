# Last week topics
    # Conditional statements (i.e. else, if, elif)
    # Simple loops

# Reviewing simple loops
    
# Ex 1
while True:
    number = int(input("Give a number, type 0 to end"))

    if number == 0:
        break

print(f"""The square of the number is {(number ** 2)}""")

# Ex 2
condition = True
counter = 1

print("Hello!")

# In this case, you can say while "condition" instead of "while True" -- it makes it easier to understand the structure for this example but otherwise is not necessary
while condition: #  With simple loops, the major important consideration to make is what is contained within or outside the loop block and when the loop is closed
    counter += 1
    print(f"the counter is now {counter}")

    if counter == 5:
        condition = False # This is where the loop breaks -- if you were to do this before printing "the counter is now {counter}" line, then only four lines would print within the loop rather than five

print("All done with the loop!")

# Ex 3
print("Hello!")

while counter <= 5: # This simplifies Ex 2
    counter += 1
    
    print(f"The counter is now {counter}")

print("All done with the loop!")

# Components of a loop
    # Initialization
    # Condition
    # Updating variables

    # Importantly, if you forget to update the variables, this often leads to an "infinite loop"

# Ex 4
number = 1 # For this example, if you want a continuous input from the user, you need to declare the "number" variable first

while number != 0: # This simplifies Ex 1 in such a way that you would no longer need a break statement within the loop, so you would establish the condition as the same time as initialization
    number = int(input("Give a number"))

    print(f"The number times 3 is {number * 3}")

# Ex 6
number = 1 # This example is NOT a model for a loop; instead it's meant to help identify what the output WOULD be for this given line of code

while number < 10: # So you set the initial condition for the loop to run so long as number is less than ten
    print(number) # You print each number while loop runs

    if number == 5: # If number is equal to five...
        break   # Immediately break from the loop and go to next line of code outside of the loop

    number += 1 # This would be skipped for any number less than 5

print("The number is now ", number) # The last line that would be printed after the loop would be "The number is now 5"

# Ex 7
while True:
    break
    print("This is never executed") # Another example of how breaking from a loop means that any following statements will not be executed

# Ex 8 
number = 1

while number < 10:
    number += 1

    if number % 3 == 0:
        continue # This is a kind of break where, for the condition in which the number is divisible by 3, the rest of the code block is not executed

    print(f"The number is now {number}") # In this case, the only outputted numbers are 2, 4, 5, 7, 8, & 10 -- numbers divisible by 3 are skipped

# Ex 9
while True:
    print("Hello")
    while True:  #This is a nested loop - there are multiple looping conditions
        print("Hello again!")
        break 
    break # Without this second break, this code would lead to an infinite loop because the break only applies to the loop it's contained in -- you need a break for EACH loop

# Indexing strings

# A string has characters between indices

# Ex 1 
name = "Haley"
print(len(name)) # Would print the number of characters in the string -- 5 in this case

# Ex 2
name = input("Give a name: ")

first = name[0] #This would provide the first character in the string
second = name[1] #This would provide the second character in the string
last = name[len(name) - 1] # This would provide the last character in the string (i.e. indexing from the end, or negative indices)

print(f"The first letter is {first}, and the second letter is {second}.")
print(f"The last letter is {last}.")

# Ex 3
name = input("Give a name: ")

index = 0

while index < len(name):
    print(name[index])
    index += 1

# Ex 4
sent = input("Give a sentence: ")

words = 1
index = 0

while index < len(sent): # Requires that the index value is always less than the number of characters in the inputted sentence
    if sent[index] == " ": # Adds a value of 1 to the words variable whenever there is a space -- since you start with one, it assumes there's a space after every word other than the last one
            words += 1
        index += 1 # Whe there is/isn't a space, the loop continues for each character by adding +1 to ensure the loop continues for the entirety of the sentence
    
print(f"The sentence has {words} words.")

# Ex 5
name = input("Give a name: ")

first_three: name[0:3]

print(f"The first three characters are {first_three}") #substrings or slicing

# Ex 6
sent = input("Give a sentence: ")

if "cat" in sent:
    print("You're talking about cats!")
    index = sent.find("cat") #.find here is a method that is being applied to search for the substring within the string object that is stored in the "sent" variable
    print(f"It starts at {index}")
else:
    print("You're talking about something other than cats.")
    # If a substring cannot be found, it returns -1
    index = sent.find("cat")
    print(index) # This should print -1

# Functions

# The basic concept of what a function does is that it allows you to repeat several statements in different parts of the program, you may use a function to do so

# Ex 1
def say_hello()
    print("Hello all!")

say_hello() # This would print "Hello all!"

# Ex 2
def say_hello()
    print("Hello all!")
    print("How are you?")

say_hello() # This would print "Hello all!" AND "How are you?" -- you can easily see how you might then build on this

# Functions thus open up modularity -- you can write a function in one script and then call it into another

# Ex 3
def ask_name():
    name = input("What is your name? ")
    print("Hello," + name + "!") # As a reminder, this is concatenation, which you can specifically do with strings

ask_name() # Now, if you call this function, it will query the user for a name first and then print the greeting message

