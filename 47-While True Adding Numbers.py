sum =  qnt = 0
while True:
    num = int(input('Enter a number and [999] To Stop '))
    if num == 999:
        break
    sum += num
    qnt += 1
print(f'The the Sum of {qnt} numbers is {sum}')
