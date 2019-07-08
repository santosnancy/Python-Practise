while True:
    number = ('Zero','one', 'Two', 'Three', 'Four', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourtenn', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty')
    n = int(input('Enter a number Between 0 to 20 '))
    while True:
        if 0 <= n <= 20:
            break
        n = int(input('Invalid Number Enter Only 0 up to 20 '))
    print(f'You Have Entered the Number {number[n]}')
    n1 = input('Do You Want To Continue?[Y/N]')
    if n1 not in 'y':
        break