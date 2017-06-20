# Matrix Algebra
import numpy as np

#Q1 - find dimensionality of various matrices
print('dimensions of A, B, C, D, u, w, are:')

A = np.matrix([[1,2,3], [2,7,4]])

print(A.shape)

B = np.matrix([[1,-1], [0,1]])

print(B.shape)

C = np.matrix([[5,-1], [9,1], [6,0]])

print(C.shape)

D = np.matrix([[3,-2,-1], [1,2,3]])

print(D.shape)

u = np.matrix([6,2,-3,5])

print(u.shape)

w = np.matrix([[1],[8],[0],[5]])

print(w.shape)

#Q2 - vector operations

v = [3,5,-1,4]

alpha = 6

print('Q2 - vector operations')

print(u + v)

print(u - v)

print(alpha*u)

udotv = np.dot(u,v)
print(udotv)

#Q3 - matrix operations

print('Q3 - matrix operations')

print('A + C cannot be added as they are not the same shape')

print(A - np.transpose(C))

print(np.transpose(C) +3*D)

print(B*A)

print('B*np.transpose(A) cannot be multiplied as the number of columns in first matrix must equal number of rows in the second matrix')

print('same for 3.6 - cannot compute multiplication of matrix B with 2 columns and matrix C with 3 rows')

print(C*B)

print(B*B*B*B)

print(A*np.transpose(A))

print(D*np.transpose(D))

