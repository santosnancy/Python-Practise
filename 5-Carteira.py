name = input('Enter your name ! ')
money = float(input('How Much Money Do You Have in Your Wallet ? '))
Dollar = 0.0003
Kwanza = 0.083
Kwacha = 0.0032

D = Dollar * money
K = Kwacha * money
Ka = Kwanza * money
print(f'Hello {name} You Have {money} UGX in Your wallet')
print(f'You Can Buy {D:.2f} Dollars')
print(f'you Can Buy {K:.2f} Kwachha')
print(f'You can Buy {Ka:.2f} Kwanzas')