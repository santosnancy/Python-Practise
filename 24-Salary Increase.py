s = int(input('Enter Your Salary! '))
if s > 1250:
    s1 = s * 10 /100
    s2 = s + s1
    print(f'Hello Your salary is {s} UGX and was increase by {s1} UGX and the new salary is {s2} UGX')
elif s <= 1250:
    e1 = s * 15 /100
    e2 = s + e1
    print(f'Hello your Salary is {s} UGX and was increased by {e1}UGX and the new salary is {e2} UGX')