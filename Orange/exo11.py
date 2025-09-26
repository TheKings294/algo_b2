try:
    note = float(input('Le note ?'))

    while note < 0 or note > 20:
        note = float(input('Le note ?'))
except ValueError:
    print('Les notes ne sont pas valide')