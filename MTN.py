def line(txt):
    print('=' * len(txt))
    print(txt.upper())
    print('=' * len(txt))


line('hello to santos bank')

deposit = 0
n = int(input('Press on to Create an Account [1]'))
if n == 1:
    name = input('Enter your full name! ')
    dob = int(input('Enter Your date of Birth'))
    gender = input('Enter Your Gender [M/F]').strip()[0]
    if gender not in 'MmFf':
        gender = input('invalid Detail Please Enter only [M/F]')
    nation = input('Enter your country! ')
    account = int(input('Enter Your account number '))
    account1 = input('Enter Your Account type [Saving / Current]')
    if account1 == 'saving':
        print('Your allowed only to deposit for a period of time')
        deposit = float(input('Enter Your value to open the Account'))
        print('Amount deposed with Success')
    elif account1 == 'current':
        print('Your are not allow open account with less than 5.000 AOA')
        deposit = float(input('Enter Your value to open the Account'))
        if deposit < 5000:
            deposit = input('Your not Allowed to open with less than 5000 AOA')
        else:
            print('Amount deposed with Success')
    print(f'Hello {name} Accounted created Successfully')
while True:
    n1 = input('Choose any option on Top to manage Your Account! ')
    if n1 == 2:
        depo = float(input('Add a ammout to your account '))
       # global deposit
        a = depo + deposit
        print(f'You have added {depo} in Your Account and now you have {a} total in your account ')
    elif n1 == 3:
        depo = float(input('Add a ammout to your account '))
        #global deposit
        a = deposit - depo
        print(f'You have withdrew {depo} in Your Account and now you have {a} total in your account ')
    n2 = input('Do You want to Continue? [Y/N] ')
    print("""Manage Your Account
        [2]Add money in Your Account
        [3]Withdraw money from your account
        [4] Exit
        """)
    if n2 not in 'Yy':
        break







