words = ""
previous = None

while True:
    word = input("Please type in a word: ")
    if word == "end":
        break
    if previous == word:
        break
    previous = word
    words += word + " "

print(words)