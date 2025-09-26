from utils import append

list = [1,2,3,4,5,6,7,8,9]
reverseList = []
lenList = len(list)

for i in list:
    append(reverseList, list[lenList - 1])
    lenList -= 1

print(reverseList)