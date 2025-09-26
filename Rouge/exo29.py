from utils import lenght

list = [4, 1, 3, 2]

for i in range(lenght(list) -1):
    for j in range(lenght(list) - i):
        if list[i] > list[i+j]:
            num = list[i]
            num2 = list[i+j]
            list[i] = num2
            list[i+j] = num

print(list)
