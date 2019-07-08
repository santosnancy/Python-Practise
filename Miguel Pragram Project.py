from math import  pow
name = input('Enter Your Name? ')
age = int(input('How Old Are You? '))
gender = input('Enter Your Gender [M/F]').upper().strip()[0]
while gender not in 'mMfF':
    gender = input('Invalid Information Only [M/F]')
high = float(input('Enter Your High![m] '))
weight = float(input('Enter Your Weight![Kg] '))
IMC = weight / pow(high, 2)
if IMC < 18.5:
    print('You Are Bellow Your Weight')
elif 18.5 <= IMC < 25:
    print('You Are on Track')
elif 25 <= IMC < 30:
    print('Above of Your Weight')
elif 30 <= IMC < 40:
    print('Your Are Obese! Be More Careful !')
else:
    print('You Are in Really Dangerous! Obesity. Practise More exercise')
print(f'Hello {name} Your IMC is {IMC:.2f}')
