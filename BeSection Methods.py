print('MAIN FUNCTION')
print('\033[1;33mF(x) = X**3 - 3X + 1')
a = int(input('\033[1;31mEnter The value of A! '))
b = int(input('Enter the value of B! '))
Xo = (a + b) / 2
FXo = Xo ** 3 - 3 * Xo + 1
X1 = (a + Xo) / 2
FX1 = X1 ** 3 - 3 * X1 - 1

print(f'The middle point value is  {Xo} \n {FXo}')







