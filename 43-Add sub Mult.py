n = 1
while n != 5:
    n1 = int(input('Enter the First number '))
    n2 = int(input('Enter the Second Number '))
    print('='* 30)
    print('''    [1]Sum
    [2]Multiplication
    [3]Greater Than
    [4]New Number
    [Exit] ''')
    n = int(input('Choose One Option On Top ! '))
    if n == 1:
        s = n1 + n2
        print(f'the Sum of {n1} and {n2} will {s}')
    elif n ==2:
        s = n1 * n2
        print(f'the Sum of {n1} and {n2} will be {s}')
    elif n == 3:
        if n1 > n2:
            print(f'the greater is {n1}')
        elif n2 > n1:
            print(f'the greater is {n2}')
    elif n == 4:
        n1= int(input('Enter the 1 Number'))
        n2 = int(input('Enter the 2 Number'))
print('CLOSING OUR APPLICATION')
