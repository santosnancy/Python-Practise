count18 = man = women = 0
while True:
    age = int(input('How Old Are You '))
    if age >= 18:
        count18 += 1
    gender = input('Enter Your Gender [M/F] ').upper().strip()[0]
    if gender == 'M':
        man +=1
    if gender == 'F'and age < 20:
        women += 1
    while gender not in 'mMFf':
        gender = input('Invalid Enter Only [M/F] ')
    n = input('Do You Want To Continue? [Y/N]')
    if n == 'n':
        break
    print('=' * 25)

print(f'We have {count18} people more than 18 Years\n{man} Men\n{women} woman(e) Less Than 20 Years')