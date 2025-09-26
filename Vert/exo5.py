try:
    number = int(input('Le nombre ?'))
    if (number % 2 == 0):
        print(f'Le nombre {number} est pair !')
    else:
        print(f'Le nombre {number} n\'est pas pair !')
except ValueError:
    print('Le nombre n\'est pas entier !')