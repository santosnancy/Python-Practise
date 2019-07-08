sum = count = 0
for lop in range(1, 500,2):
    if lop % 3 == 0:
        sum += lop
        count += 1
print(f'\033[1;31mThe sum of {count} numbers is {sum}')



