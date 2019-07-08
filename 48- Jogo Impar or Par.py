win = 0
while True:
    from random import randint
    computer = randint(1,10)
    Player = int(input('Enter a Number '))
    game = input('Par or Impar [P/I] ')
    while game not in 'PpIi':
        game = input('Invalid Enter Only [P/I]')
    result = Player + computer
    if game == 'p':
        if result % 2 == 0:
            win +=1
            print(f'You Have Won the Computer')
        else:
            print('You have Lost')
            break
    elif game == 'i':
        if result % 2 == 1:
            win +=1
            print('You have have Won the Computer')
        else:
            print(f'You have Lost')
            break
print('='* 60)
print(f'Computer payed {computer} And Played {Player} and The Sum is {result} You Won {win} Time(s)')
