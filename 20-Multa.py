v = int(input('Enter The Speed of your Car '))
if v > 80:
    tax = 7.00
    v1 = v - 80
    tax1 = v1 * tax
    print(f'You have passed the Limit of {v1} Km and will pay Tax of {tax1} UGX')
else:
    print('You Are on Right Track! Good Luck')
