greater = less = 0
num = []
for lop in range(0,5):
    num.append(int(input(f'Enter a the {lop} Number ')))
    if lop == 0:
        greater = less = num[lop]
    else:
        if num[lop] > greater:
            greater = num[lop]
        if num[lop] < less:
            less = num[lop]
print('='* 40)
print(f'the values are {num}')
print(f'the Greater value is {greater} in position ',end='')
for i,a in enumerate(num):
   if i == greater:
       print(f'{i}......',end=' ')
print()
#print(f'the Less Value  is {less} in position ',end='')
#for i ,a in enumerate(num):
   # if i == less:
       # print(f'{i}')
