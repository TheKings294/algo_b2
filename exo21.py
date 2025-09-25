try:
    word = str(input('Word: '))

    if word.isdigit():
        print('Error')
        exit()

    reverseWord = word[::-1]
    staus = 0

    for i in range(len(reverseWord)):
        if reverseWord[i] == word[i]:
            staus = 1
        else:
            staus = 0

    print("Palindrome" if staus == 1 else "False")
except ValueError:
    print('Not an string')