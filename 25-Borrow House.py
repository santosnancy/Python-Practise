name = input('enter your name ')
House = int(input('Enter The Price of the House! UGX '))
Sal = int(input('How Much Do You Get per Month? UGX '))
Tp = int(input('For How Long Do You Want To Pay This House? '))
min = Sal * 30 / 100
prestacao = House / (Tp * 12)


if prestacao < min:
    print(f'\033[1;32m Hello {name} Your  are Qualified To Buy This House')
    print(f'To Pay a House of {House} UGX in {Tp} Years The Fine Will be {prestacao:.2f}UGX')
elif prestacao > min:
    print(f'Hello {name} Your  are Not Qualified To Buy This House')
    print(f'To Pay a House of {House} UGX in {Tp} Years The Fine Will be {prestacao:.2f}UGX')

print('Thank You, Come Again')


