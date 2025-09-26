from utils import lenght

list = [8, 1, 20, 3]
min = list[0]
max = list[0]

for i in range(lenght(list)):
    if list[i] < min:
        min = list[i]
    if list[i] > max:
        max = list[i]

print(min, max)