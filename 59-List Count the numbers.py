count = 0
num = []
while True:
    num.append(int(input('Enter A Number ! ')))
    count += 1
    n = input('Do You What to Continue? [Y/N]')
    if n in 'Nn':
        break
print('=' * 50)
print(f'You have entered {count} numbers')
print(f'{num}')
print(f'The numbers in Reverse Order is {sorted(num,reverse=True)}')
if 5 in num:
    print('There is number (5) in this list')
else:
    print('There is no Number (5) in the list')