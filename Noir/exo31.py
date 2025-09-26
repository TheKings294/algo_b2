santence = '((a+b)*()()*(c-d))'
open = 0
close = 0

for i in santence:
    if i == '(':
        open += 1
    elif i == ')':
        close += 1

    if close > open:
        print('Incorrect')
        exit()

if open == close:
    print('The sum of () is correct')
else:
    print('The sum of () is incorrect')