import re

try:
    binary = str(input('Binaire ?'))
    puissance = len(binary) - 1
    decimal = 0
    pattern = r'^[01]+$'

    if not re.match(pattern, binary):
        print('Le binaire n\'est pas valide')
        exit()

    for number in binary:
        if number == "1":
            decimal = 2**puissance
            puissance -= 1

    print(decimal)
except ValueError:
    print('Le nombre n\'est pas binaire !')