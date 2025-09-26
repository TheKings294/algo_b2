from utils import append, sum_list, lenght

try:
    noteList = []
    append(noteList, float(input('Le nombre 1 ?')))
    append(noteList, float(input('Le nombre 2 ?')))
    append(noteList, float(input('Le nombre 3 ?')))

    for note in noteList:
        if note < 0 or note > 20:
            print('Les notes ne sont pas valide')
            exit()

    print(round(sum_list(noteList)/lenght(noteList), 2))
except ValueError:
    print('Le nombre n\'est pas entier !')