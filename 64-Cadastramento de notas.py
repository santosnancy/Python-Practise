cadastro = [[], []]
while True:
    cadastro[0].append(input('Enter Your Name '))
    cadastro[1].append(float(input('Enter Your Grade ')))
    n = input('Do You Want to Continue?[Y/N] ').upper().strip()[0]
    print('=' * 20)
    if n in 'nN':
        break
for pos, name in enumerate(cadastro[0]):
    print(f'{name}',end='')
for pos, grade in enumerate(cadastro[1]):
    print(f'{grade:.>30}')
