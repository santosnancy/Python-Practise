from random import randint

items = ('Stone','Paper','Scissors')
computer = randint(0, 2)
print('''Welcome To  Our Game !!!!!!!
         Lets Pay Now
         [0]Stone
         [1]Paper
         [2]Scissors ''')
n1 = int(input('Please Start Play '))
print(f'the computer played {items[computer]}')
print(f' You Played {items[n1]}')
if  computer == 0: # Computer Played Stone
    if n1 == 0:
        print('Its a Draw')
    elif n1 == 1:
        print('You Have Won the Computer')
    elif n1 == 2:
        print('The Computer Has Won')
    else:
        print('INVALID')

elif computer == 1: # Computer Played Paper
    if n1 == 0:
        print('The Computer Have Won')
    elif n1 == 1:
        print('Its a Draw')
    elif n1 == 2:
        print('You Have Won The Computer')
    else:
        print('INVALID')

elif  computer == 2: # Computer Played Scissors
    if n1 == 0:
        print('You have one the Computer')
    elif n1 == 1:
        print('the computer have one')
    elif n1 == 2:
        print('Its a Draw')
    else:
        print('INVALID')

print('=' * 10, 'END', '=' * 10)

