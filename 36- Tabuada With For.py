while True:
    num = int(input('Enter a Number Of Your Choice ! '))
    for lop in range(1, 13):
        t = num * lop
        print(f'{num} X {lop} = {t}')
    num1 = input('Continue [S/N]? ')
    if num1 == 'n':
        break
print('ENDING OF OUR PROGRAM')