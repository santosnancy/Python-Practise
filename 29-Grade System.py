name = input('Enter a name ')
age = int(input('How Old Are You ?'))
gender = input('Enter your Gender !')
while gender not in "fFmM":
    gender = input('Invalid Data ! Please enter only M or F ')
course1 = float(input('Enter your Grade for midsemester '))
course2 = float(input('Enter Your final Exams result '))
grade = (course1 + course2)/2
if grade >= 10:
    print(f'hello {name} you had {course1} and {course2} and your final result is {grade}')
    print('You Have Passed \n Congratulations !!!!!!!!')
elif grade == 8 or 9:
    print(f'hello {name} you had {course1} and {course2} and your final result is {grade}')
    print('You Have to make a special Exams')
else:
    print(f'hello {name} you had {course1} and {course2} and your final result is {grade}')
    print('You Have Failed')


