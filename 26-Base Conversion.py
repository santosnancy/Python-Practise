num = int(input('enter Any Number '))
print('''\033[1;32m
[1]Binary
[2]hexadecimal
[3]Octadecimal''')
n = int(input('Choose Any Option On Top! '))
A = bin(num)
B = hex(num)
C = oct(num)
if n == 1:
    print(f'the binary of {num} is {A[2:]}')
elif n == 2:
    print(f'the Hexadecimal of {num} is {B[2:]} ')
elif n == 3:
    print(f'the Octadecimal of {num} is {C[2:]}')
