count = 0
num = ((int(input('Enter The First Number '))),
      (int(input('Enter the Second Number '))),
      (int(input('Enter The Third Number '))),
      (int(input('Enter the Last Number '))))
print(f'The numbers are: {num}')
print(f'The Number  (9) Appear {num.count(9)} Time(s)')
if 3 in num:
 print(f'The First Number (3) Appeared in Position {num.index(3)}')
else:
    print('There is No Number (3) in This List')
print(f'The Pares Numbers Are ', end='')
for lop in num:
    if lop % 2 == 0:
        print(f'{lop}',end='')
