num = 'Y'
sum = qnt = less = greater = 0
while num == 'Y':
    num1 = int(input('Enter  number! '))
    num = input('Do You Want To Continue[Y/N]').upper().strip()[0]
    qnt += 1
    if qnt == 1:
         greater =less = num1
    else:
       if num1 > greater:
             greater = num1
       if num1 < less:
           less = num1

    sum += num1
    Average = sum / qnt
print(f'The sum of {qnt} number is {sum} and the Average is {Average} The Greater is {greater} and the lesss is {less}')


