average =  female =  max =  nameold = 0
for lop in range(1,3):
    print(f'='* 5, lop,'Person','='*5)
    name = input('enter your the o name! ')
    age = int(input('How Old Are You? '))
    gender = input('Enter Your Gender[M/F]! ')
    average += age / 4
    if gender == 20 and gender == 'f':
        female +=1
    if gender in 'M' and max > age:
        age = max
        name = nameold

print(f'the Average of the all Age is {average} ')
print(f'we have {female} with 20 years')