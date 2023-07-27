import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
c = np.zeros((3, 3))
d = np.arange(0,9)
'''
print("Here is matrix A :")
print(a)
print("Here is matrix B :")
print(b)
print("Here is matrix A X B :")
for i in range(3):
    for j in range(3):
        sm = 0
        for k in range(3):
            sm = sm + a[i][k] * b[k][j]
        c[i][j] = sm

print(c)
print("Here is matrix B X A :")
print(b.dot(a))
print("Dimension of array", c.ndim)
print("Size of array", c.size)
print("Item size of array", c.itemsize)
print("Data type of array", c.dtype)
print(d)
'''

print(c)