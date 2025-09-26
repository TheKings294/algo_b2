sentance = str(input("Enter a sentence: "))

dico = {}

for letter in sentance:
    if letter not in dico:
        dico[letter] = 1
    else:
        dico[letter] += 1

for letter in dico:
    print(letter, end="")
    print(dico[letter], end="")