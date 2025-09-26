voyelle = ['a', 'e', 'i', 'o', 'u', 'y']
word = "Bonjour 2025"
voyelleCount = 0
consonneCount = 0
numberCount = 0
spaceCoutn = 0


for letter in word:
    match letter:
        case _ if letter in voyelle:
            voyelleCount += 1
        case _ if letter.isdigit():
            numberCount += 1
        case _ if letter == ' ':
            spaceCoutn += 1
        case _ if letter not in voyelle and letter.isalpha():
            consonneCount += 1

print('Voyelles: ', voyelleCount)
print('Consonnes: ', consonneCount)
print('Numbers: ', numberCount)
print('Space: ', spaceCoutn)