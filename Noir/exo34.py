list = [2, 4, 6, 8, 10]
find = 8
status = 0
count = 0

first = 0
last = len(list) - 1

while status != 1 and first <= last:
    mid = (first + last) // 2
    if list[mid] == find:
        count += 1
        status = 1
    else:
        count += 1
        if find > list[mid]:
            first = mid+1
        else:
            last = mid-1

print(count)