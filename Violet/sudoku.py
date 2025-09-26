solution = [
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9]
]

def how_many_in_the_line(line, number):
    count = 0
    for i in line:
        if i == number:
            count += 1

    return True if count == 1 else False

def is_valid_sudoku(board):
    for tab in board:
        for i in tab:
            if not how_many_in_the_line(tab, i):
                return 'Invalide'

    listCol = [[],[],[],[],[],[],[],[],[]]

    for i in range (0, len(board)):
        for j in range (0, len(board[i])):
            listCol[i].append(board[j][i])

    for line in listCol:
        for j in line:
            if not how_many_in_the_line(line, j):
                return 'Invalide'

    listCube = []

    for i in range (0, len(board), 3):
        for j in range (0, len(board), 3):
            bloc = []
            for k in range (i, i+3):
                for l in range (j, j+3):
                    bloc.append(board[k][l])

            listCube.append(bloc)

    for line in listCube:
        for j in line:
            if not how_many_in_the_line(line, j):
                return 'Invalide'

    return 'Valide'









print(is_valid_sudoku(solution))