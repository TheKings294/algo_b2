from utils import lenght, append

list = [-3, 5, 0, 7,-1]
listPositiv = []

for i in range (lenght(list)):
    if list[i] > 0:
        append(listPositiv, list[i])

print(listPositiv)