voyelle = ['a', 'e', 'i', 'o', 'u', 'y']
word = "Bonjour"
lowerWord = word.lower()
numberVoyelle = 0

for letter in lowerWord:
    if letter in voyelle:
        numberVoyelle += 1

print(numberVoyelle)