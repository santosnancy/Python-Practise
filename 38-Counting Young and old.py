y = o = 0
from datetime import date
for lop in range(1, 7):
    birth = int(input(f'Enter  the {lop}o Birth Date! '))
    year = date.today().year
    age = year - birth
    if age >= 21:
        o += 1
    else:
        y += 1
print(f'Hello We have {o} people that are old and {y} people that are young')
