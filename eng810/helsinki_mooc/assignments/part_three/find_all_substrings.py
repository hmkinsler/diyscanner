word = input("Please type in a word: ")
char = input("Please type in a character: ")

while char in word:
    start = word.find(char)
    if (len(word) - start) < 3:
        break
    end = start + 3
    print(word[start:end])
    start += 1
    word = word[start:]
