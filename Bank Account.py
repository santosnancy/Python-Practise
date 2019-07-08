CountAccount = 0
account = list()
while True:
    print('=' * 10, 'WELCOME TO ANGOLAN BANK', '=' * 10,)
    print('SELECT ONE OPTION BELLOW')
    print('''
    [1] Open an Account
    [2] Balance Enquiry
    [3] Deposit
    [4] Withdrawal
    [5] Close an Account
    [6] Show All Account
    [7] Quit ''')
    n = int(input('Enter Your Choice! '))
    if n == 1:
        n1 = account.append(input('Enter Your First name !'))
        n2 = account.append(input('Enter Your Last name! '))
        n3 = account.append(float(input('Enter Your Initial Balance! ')))
        CountAccount += 1
        for pos, name in enumerate(n1):
            print()
        #print('Congratulations Your Account Was Created Successfully')

#print('See You Dear Customer, Hope we meet Again')
