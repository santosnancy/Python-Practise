from random import randint
n = randint(1, 2)
n1 = int(input('Enter a number between 1 to 5 '))
if n == n1:
    print(f'You Played {n1} and PC {n}')
    print('\033[1;32mYou have Won')
else:
    print(f'You Played {n1} and PC {n}')
    print('\033[1;34mYou Lost')


