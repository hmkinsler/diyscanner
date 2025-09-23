# Review of concepts from part 3
# - Repetition with while loops
# - Break vs. continue in loops
# - Nested loops
# - Indexing strings
# - Extracting characters and substrings
# - Introduction to own functions

# Paremeters vs. arguments
def shout(message): #in this case, the message is the parameter
    print(message + "!!!")

# You generally want to be mindful of how many parameters you include in a single function -- if you have a significant number of them, it may be worth exploring alternatives

def get_sum(first, second): # Example with two parameters
    print(first + second)

shout("Hello all") # This is where you are using an argument

get_sum(2, 5) # And here are two arguments

# Return statements allow more flexibility when writing functions however, allowing us to output the results of a given function without requiring a print statement in every case

def get_sum(first, second):
    return first + second # This return statement calculates the sum as part of the function

# But to actually see the result, you have to still provide a way for the output to be read to the user

value = get_sum(2, 5) # This stores the result as a variable
print(value) # And then prints the variable for the user

# And if we wanted to make this more complex and involve multiple operations...

value = get_sum(2, 5) * 2 # Now there's an additional operation taking place
print(value) # And you print the result of that and would expect an output of 14

# And you could print this more directly, too:
print(get_sum(2, 5) * 2)

# The difference between return and print statements is particularly key

# Print statements are used to output a value in the output stream

# The return statement, however, simply returns the value from a function and when used also immedately terminates the execution of the function

def get_sum(first, second):
    value = first + second
    return value
    print("This is not executed.") # Because return statement terminates, this never prints

s = get_sum(1, 2) # This variable would store the returned value for these arguments

# which you could then add to...
while s <= 100:
    s += 1
    print(s)

# Another example working with strings
def concatenate(first, second):
    sentence = first + second
    return sentence

s = concatenate("Hi, ", "all")

print(s) # Expected output would be "Hi, all"

# Python is dynamically typed, meaning that the data type is assigned based on what the value is that's assigned to the variable

# This is different from statically typed languages like Java, which require for the data type to always be explicitly expressed

# Because the type is not always explicit in Python, which can pose particular issues in tracing what a function or program is doing, it can be helpful to include type hints in the functions you write

def get_sum(first: int, second: int): # This includes type hints
    value = first + second # Type hints do not force a data type to be assigned...
    return value 

# ...But they can offer some info to the programmer about what should type should be used when writing arguments as they call a function

s = get_sum(1, 2)
print(s)

# Type hints can include...
# - int (integer)
# - float (floating point number)
# - str (string)
# - bool (boolean value)

def repeat(message: str, n: int): # These type hints ask for a string and integer argument
    msg = ""
    index = 0
    while index < n:
        msg += message
        index += 1

    return msg

r = repeat("Hi! ", 3)
print(r) # Expected output would be "Hi! Hi! Hi! "

# You can also write type hints that clarify what type you would expect from a return value
def repeat(message: str, n: int) -> str: # Expected return value would be a string
    msg = ""
    index = 0
    while index < n:
        msg += message
        index += 1

    return msg

r = repeat("Hi! ", 3)
print(r) # Expected output would be "Hi! Hi! Hi! "

# The use of type hints is really heavily encouraged because they make it easier to identify and prevent errors, improve the readibility of code, and make it easier for programmers to adhere to Pythonic logic and syntax

# Storing data beyond a single variable

name1 = "Mike"
name2 = "Jon"

# ...
name3 = "Matt" # While this is a Pythonic way to store lots of names / data, it's not very efficient or practical for most cases

# For example, if you wanted to add a surname to all of these names, you'd have to do that to each individual variable, like this:

name1 += "Smith"
name2 += "Smith"

# This is where data structures come in, which allow us to more readily store data so that we can make changes to our data all at once with functions, methods, etc.

# Lists: Lists are collections of homogeneour items and can be created with bracket notation

fruits = ["orange", "banana", "apple"] # list with string type
values = [1, 2, 3, 4, 5] # list with integer type
decimals = [1.1, 2.2, 3.3, 4.4, 5.5] # list with float type
truths = [True, True, False, True] # list with boolean type

# Lists offer various operations, like finding the index of an item

print(values[0]) # expected output would be 1

print(fruits[0]) # expected output would be "orange"

print(decimals[-1]) # expected output would be 5.5

# One difference between lists and strings is that we can assign values with lists
fruits[0] = "Plum"

# The index for the list does have to exist in order to assign a value-- otherwise will produce index out of range error

# There are methods for adding items to a list, however
fruits.append("Mango")

print(fruits) # Expected output would have "Mango" added at index 3

# So you could loop to add items to a list:
numbers = []

while True:
    num = int(input(" Give a number, -1 to stop"))

    if num == -1:
        break

    numbers.append(num)

print(numbers)

# Can use the insert method as well
numbers = [1, 2, 3, 4, 5]

numbers.insert(0, 10) # inserts integer 10 at index 0, shifting index for everything else forward

print(numbers) # Expected output would be "[10, 1, 2, 3, 4, 5]"

# Can use len to find number of items in a list
numbers = [1, 2, 3, 4, 5]
index = 0

while index < len(numbers):
    print(numbers[index])
    index += 1

# Example with strings
animals = ["dog", "cat", "cow", "sheep", "giraffe"]
all_animals = ""

for animal in animals: # In the for loop, each list item is assigned to variable animal
    all_animals += animal + "" # This concatenates all the list items into a single variable

print(all_animals)

# Example for loop with numbers
numbers = [1, 2, 3, 4, 5]
sum = 0

for number in numbers:
    sum += number # adds each number from list to sum variable

print(sum) # Expected output would be 15

# Example for loop with strings
name = "Alex"

for character in name:
    print(character)

# And breaks in for loops can be useful for identifying a particular item in a list that meets a given criteria
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for value in values:
    if value % 7 == 0:
        print(value)
        break # This would stop the loop as soon as the first item divisible by 7 is printed

# The range function can be used to create an iterable sequence
r = range(10) 
print(r) # Prints numbers 0 to 9

r = range(1, 10) # Prints numbers 1 to 9

# Example of operation with range
s = 0

for i in range(1, 100001):
    s += i

print(s) # Prints sum of all items in range that are stored in variable s

# You can also create a list from values in a range
r = range(10, 21)

values = list(r) # Now you can avoid having to type all numbers 10-20 individually

print(values)

# The range function also accepts a step parameter
r = range(10, 21, 2)

values = list(r)

print(values) # Prints values 10 - 20 in steps of 2 --> 10, 12, 14, 16, 18, 20

# And you can have negative steps
r = range(10, 0, -1)

values = list(r)

print(values) # Starts from 10 and counts down to 1

# Lists are sortable
values = [10, 4, 5, 3, 8, 2, 3]

values.sort()

print(values) # Sorts in ascending order

# Can sort strings as well
names = ["Matt", "Anne", "Mary", "Caleb"]

names.sort()
print(names) # Sorts names into alphabetical order -- does presume consistent case for names

# And you can also sort into a new variable to maintain the original list
names = ["Matt", "Anne", "Mary", "Caleb"]
names_sorted = sorted(names)

print(names_sorted)

# Pop functions to remove items from lists
names.pop() # Removes final item from the list
names.pop(2) # Removes third item from the list -- "Mary" in this case

# You can store what you remove as a variable if needed
removed = names.pop(2)
print(removed)

# Can use remove function to remove the item by name
names.remove("Mary")

# Main difference between strings and lists is that strings are immutable -- you cannot change the content of a string after it's been created like you with a mutable data structure like a list

# Count method
sentence = input("Please type a sentence: ")
spaces = sentence.count(" ")
print(f"There are {spaces + 1} words in that sentence.")

# Replace method -- specifically used with strings
sentence = "This is a long sentence."
sentence2 = sentence.replace("long", "really long") # You have to assign to a new variable

print(sentence2) # Prints "This is a really long sentence"

# Or you could store in a new variable that replaces the previous variable object
sentence = "This is a long sentence."
sentence = sentence.replace("long", "really long")

print(sentence) # Prints "This is a really long sentence"

# Upper case function
name = "peter"

name = name[0].upper() + name[1:]
print(name)

# Formatting output formats

# Concatenation
name "Mark"
age = 32

print("Hi " + name + " you age is" + str(age) + " years")

# Separating with commas
print("Hi", name, "your age is", age, "years")

print("Hi", name, "your age is", age, "years", sep="")

# F-strings
print(f"Hi {name} your age is {age} years")
