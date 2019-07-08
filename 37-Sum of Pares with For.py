sum = count =0

for lop in range(1,7):
    num = int(input(f'Enter the {lop}o number '))
    if num % 2 == 0:
        sum += num
        count += 1
print(f'the sum of {count} numbers pares is {sum}')
