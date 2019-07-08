gender = input('enter your gender[M/F]').upper().strip()[0]
while gender not in 'MmFf':
   gender = input('Invalid Info Please enter Only [M/F]')
print('Register Successfully')

