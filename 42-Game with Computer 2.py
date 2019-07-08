from random import randint
n1 = 1
while n1 != 0:
    n = randint(1,10)
    n1 = int(input('Enter A Number Between 1 to 9 '))
    if n1 == n:
            print(f'\033[1;32mYou Played {n1} and the Played {n}\nCongratulations You Won')
    else:
            print(f'\033[1;31mYou Played {n1} and the Played {n}\nYou Have Lost')

