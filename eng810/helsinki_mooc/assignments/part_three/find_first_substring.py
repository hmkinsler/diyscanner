word = input("Please type in a word: ")
char = input("Please type in a character: ")

if char in word:
    start = word.find(char)
    if (len(word) - start) >= 3:
        end = start + 3
        print(word[start:end])