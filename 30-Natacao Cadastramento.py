from datetime import date
name = input('Enter Your Name ')
birth = int(input('Enter Your Birth Date '))
A = date.today().year
year = A - birth
if year <= 9:
    print(f'Hello {name} You are  {year} Old and you are MIRIN')
elif year == 14:
    print(f'Hello {name} You are  {year} Old and you are INFANTIL')
elif year == 19:
    print(f'Hello {name} You are  {year} Old and you are JUNIOR')
elif year == 20:
    print(f'Hello {name} You are  {year} Old and you are SENIOR')
elif year > 20:
    print(f'Hello {name} You are  {year} Old and you are MASTER')
