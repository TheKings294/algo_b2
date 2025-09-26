try:
    number1 = int(input('Le nombre 1 ?'))
    number2 = int(input('Le nombre 2 ?'))
    print(min(number1, number2))
except ValueError:
    print('Le nombre n\'est pas entier !')