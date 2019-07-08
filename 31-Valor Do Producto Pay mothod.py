pr = int(input('Enter the price the product!UGX '))
print('''\033[1;32m          [1]Cash/Prestacao
          [2]Cheque
          [3]Visa Card
          [4]Cash''')
n1 = int(input('\033[34mHow Dou You Want to Pay ?'))
if n1 == 1:
    d = pr * 5 / 100
    d1 = pr - d
    print(f'\033[1;31m the Product price is {pr}UGX the discount of 5 % is {d}UGX and you will pay now {d1}UGX')
elif n1 == 2:
    d = pr * 15 / 100
    d1 = pr - d
    print(f'the Product price is {pr}UGX the discount of 5 % is {d}UGX and you will pay now {d1}UGX')
elif n1 == 3:
    d = pr * 20 / 100
    d1 = pr - d
    print(f'the Product price is {pr}UGX the discount of 5 % is {d}UGX and you will pay now {d1}UGX')
elif n1 == 4:
    print(f'Hello There is no Discount You Still Pay {pr}UGX')