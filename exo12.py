result = 1
try:
    number = int(input('Le numero ?'))

    for i in range(number):
        result = result * (number - i)

    print(result)
except ValueError:
    print('L\'entier n\'est pas valide')