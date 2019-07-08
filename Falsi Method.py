def func(x):
    return pow(x, 3) - 3 * x + 1
    # Here return the value of the function

print('This is The Main Bisection Equation')
print('\033[1;32mX^3 + 3X + 1')
Xo = float(input('Enter the First Interval Value to the root! '))
X1 = float(input('Enter the Second Interval Value  to the root'))
iter = int(input('Enter the Number of iteration You want to perform! '))
a = 2
b = 4

L1 = Xo
L2 = X1
r = f1 = f2 = f3 = 0
ctr = 1
#Here we going to check if the approximations are the root or not
if func(L1) == 0:
    r = L1
else:
    if func(L2) == 0:
        r = L2
    else:
        # Here Where was implemented the algorithm mentioned above
        while ctr <= iter:
            f1 = func(L1)
            r = (a * L1 - b * L2) / L1 - L2
            f2 = func(r)
            f3 = func(L2)
            if f2 == 0:
                r = f2
                break
            print(f'The Root After {ctr} Iteration is {r:.2f}')
            if f1 * f2 < 0:
                L2 = r
            else:
                if f2 * f3 < 0:
                    L1 = r
                    ctr += 1
    print(f'\033[1;31mThe Approximation to the root is { r:.2f}')










