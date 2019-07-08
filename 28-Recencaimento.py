from datetime import date
name = input('Enter Your Name! ')
birth = int(input('Enter Your Birth Date! '))
A = date.today().year
Year = A - birth
min = 18
if birth == min:
    print(f'Hello {name} You have Born in {birth} and you  {Year} Years,\nYour on Time to Register! Congratulations')
elif Year > min:
    min1 = Year - min
    b =  A - min1
    print(f'Hello {name} You have Born in {birth} and you are {Year} Years And You Are {min1} Late\nYour Time was Registration Was {b}')
elif Year < min:
    min2 = min - Year
    print(f'Hello {name} You Will Turn {Year} Years Still Remain {min2} Years To register ')

