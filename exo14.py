try:
    number = int(input('Number ?'))
    result = 0

    for i in range(1 ,number+1):
        result += i

    print(result)
except ValueError:
    print('Nombre non valide')