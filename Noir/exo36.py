numberA = int(input("Number A ? "))
numberB = int(input("Number B ? "))
print('Whitch operator :')
print('[1] : AND')
print('[2] : OR')
print('[3] : XOR')
choice = int(input("What operator do you choose? "))
result = 0

match choice:
    case 1:
       result = numberA & numberB
    case 2:
        result = numberA | numberB
    case 3:
        result = numberA ^ numberB

print(result)