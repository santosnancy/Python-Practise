name = input('enter Your Name! ')
age = int(input('How Old Are You? '))
gender = input('Enter your Gender [F/M]')
while gender not in 'mf':
    gender = input('Invalid Information Enter only F or M ')
print(f'Hello {name} Your are {age} and you are {gender.upper()}')