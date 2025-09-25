try:
    decimal = int(input('Decimal :'))
    hex = ""
    hex_digits = "0123456789ABCDEF"

    if decimal == 0:
        print("O")
        exit()

    while decimal > 0:
        remainder = decimal % 16
        hex = hex_digits[remainder] + hex
        decimal //= 16

    print(hex)
except ValueError:
    print('Unvalid Number')