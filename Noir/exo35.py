import random

number = random.randint(1,20)
userChose = int(input("What number do you choose?"))

while userChose != number:
    if userChose == number:
        break
    elif userChose < number:
        print("Plus")
        userChose = int(input("What number do you choose?"))
    elif userChose > number:
        print("Minus")
        userChose = int(input("What number do you choose?"))

print('You win !')