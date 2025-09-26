try:
    number1 = int(input('Number 1: '))
    number2 = int(input('Number 2: '))
    result = 1

    for i in range(number2):
        result *= number1

    print(result)
except ValueError:
    print('Nombre non valide')