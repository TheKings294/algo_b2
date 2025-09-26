number = 18

if number <= 0:
    print('O')
    exit()

while number > 1:
    if number % 2 != 0:
        print('Not an puissance')
        exit()
    number //= 2

print('Is an puissance')