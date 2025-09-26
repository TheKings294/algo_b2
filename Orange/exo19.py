try:
    decimal = int(input('Decimal :'))
    binary = ""

    if decimal == 0:
        print("O")
        exit()

    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal //= 2

    print(binary)
except ValueError:
    print('Unvalid Number')