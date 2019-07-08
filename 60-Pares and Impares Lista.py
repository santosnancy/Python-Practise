num = []
pares = []
imp = []
while True:
    num.append(int(input('Enter a number! ')))
    n = input('Do You Want to Continue?[Y/N]')
    if n in 'Nn':
        break
for p,el in enumerate(num):
    if el % 2 == 0:
        pares.append(el)
    elif el % 2 == 1:
        imp.append(el)

print(f'the Whole List is {num}')
print(f'the Pares Numbers Are: {pares}')
print(f'The Impares Numbers Are: {imp}')

