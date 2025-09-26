try:
    year = int(input('Year ?'))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print('Annee bisextile')
    else:
        print('Annee non bisextile')
except ValueError:
    print('L\'annee n\'est pas valide')
