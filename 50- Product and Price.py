tgast =  prodc = low = cont =0
cheap = ''
while True:
    print('='* 26)
    product = input('Enter The name of Product! ')
    price = int(input('Enter the Price: UGX '))
    cont +=1
    if price > 1000:
        prodc += 1
    tgast += price
    if cont == 1 or price < low:
        low = price
        cheap = product
    n = input('Do You Want to Continue[Y/N]')
    if n not in 'y':
        break
print(f'\033[1;32mYour Total Cost is {tgast} UGX m')
print(f'We have {prodc} products That cost More Than: 1000 UGX')
print(f'the low price is {low} and product name is {cheap}')
