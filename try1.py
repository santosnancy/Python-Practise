pares = []
impares = []
for lop in range(0,4):
    num = int(input('enter a whole number '))
    if num % 2 ==0:
        pares.append(num)
    else:
        impares.append(num)
print(f'the pares number are {pares}')
print(f'the impares numbers are {impares}')



