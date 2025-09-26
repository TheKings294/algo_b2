n = int(input("Enter an number :"))
tab = []

for i in range(2, n):
    tab.append(i)

for i in tab:
    if i % 2 == 0 and i != 2:
        tab.remove(i)

for i in tab:
    if i % 3 == 0 and i != 3:
        tab.remove(i)

for i in tab:
    if i % 5 == 0 and i != 5:
        tab.remove(i)

for i in tab:
    if i % 7 == 0 and i != 7:
        tab.remove(i)

print(tab)