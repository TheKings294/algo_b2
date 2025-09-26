try:
    noteList = []
    noteList.append(float(input('Le nombre 1 ?')))
    noteList.append(float(input('Le nombre 2 ?')))
    noteList.append(float(input('Le nombre 3 ?')))

    for note in noteList:
        if note < 0 or note > 20:
            print('Les notes ne sont pas valide')
            exit()

    print(round(sum(noteList)/len(noteList), 2))
except ValueError:
    print('Le nombre n\'est pas entier !')