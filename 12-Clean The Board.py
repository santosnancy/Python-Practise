from random import choice
n1 = input('enter your 1o name ')
n2 = input('enter your 2o name ')
n3 = input('enter your 3o name ')
n4 = input('enter your 4o name ')
students = [n1, n2, n3, n4]
lo = choice(students)
print('='* 20)
print(f'The Chosen Student is {lo}')

