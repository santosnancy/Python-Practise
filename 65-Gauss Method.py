import numpy as np
def line():
    print('===' * 9)

A = np.array([[7, 3],
             [5, 4],
              ])
B = np.array([
    [1, 5],
    [12, 3]
])
print('Here we Find out the Determinate of A and B! ')
DetA = A[0][0] * A[1][1]
DetA1 = A[1][0] * A[0][1]
Detresult = DetA - DetA1
print(f'the Result of Delta of Matrix A is {DetA},{DetA1} \n{Detresult}')






