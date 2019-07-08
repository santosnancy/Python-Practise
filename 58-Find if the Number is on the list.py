num = []
while True:
    n =(int(input('Enter A Number ! ')))
    if n not in num:
        num.append(n)
        print('Numbers Entered with Success')
    else:
        print('Duplicated Value! Wont Be Added')
    n = input('Do You Want To Continue?[Y/N]')
    if n in 'Nn':
        break

print('=' * 40)
print(f'The numbers Are :{sorted(num)}')