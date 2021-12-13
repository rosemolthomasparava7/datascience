import numpy as np

M = np.array([[2,3,4], [3,45,8], [4,8,78]])
print("Matrix M\n", M)
# Transposing the Matrix M
print('\n\nTranspose as M.T\n', M.T)

if M.T.all() == M.all():
    print("The matrix is symmetric")
else:
    print("The given matrix is Not symmetric")
A = np.array([[1,3,7], [3,-5,8]])
if A.T.all() == ~A.all():
    print("The matrix is skew symmetric")
else:
    print("The given matrix is Not skew symmetric")

    