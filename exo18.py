list = [10, 12, 8]

len = 0
for i in list:
    len += 1

result = 0
for i in range(len):
    result += list[i]

print(result/len)