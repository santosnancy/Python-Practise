
from random import randint
num = (randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6),randint(1, 6))
lop = max(num)  # Max is Only Used in List  to check the bigger No on the list
lop1 = min(num)  # Min is Only Used in List to check the Less No on the list
print(f'The All 5 numbers Given By the List is {num}\nthe Greater  is No is {lop} and the Less No is {lop1}')
