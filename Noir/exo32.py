watingList = []
start = 1


def addPoeple(name):
    watingList.append(name)

def removePoeple(name):
    if name in watingList:
        watingList.remove(name)
    else:
        print('Poeple not found')

while start == 1:
    print('[1]: New user \n [2]: Delete user \n [3]: Quit')
    number = int(input('Enter your choice: '))

    match number:
        case 1:
            name = str(input('Enter your name: '))
            addPoeple(name)
            print('Poeple added')
            print(watingList)
        case 2:
            name = str(input('Enter your name: '))
            removePoeple(name)
            print('Poeple removed')
            print(watingList)
        case 3:
            exit()