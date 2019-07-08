v = float(input('Enter The Distance of Your Trip Per Km! '))
if v <= 200:
    p = v * 0.50
    print(f'You Will Pay {p} UGX For the ticket')
elif v > 200:
    p1 = v * 0.45
    print(f'You Will Pay {p1} UGX For the Ticket')
