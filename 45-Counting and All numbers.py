sum = 0
num = 1
while num != 999:
    num = int(input('Enter Any Number And [999] To Stop '))
    if num != 999:
     sum += num
print(f'\033[1;32mThe sum of all number is {sum}')
