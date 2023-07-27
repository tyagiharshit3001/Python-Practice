# Matrix decleration and definitation using vector
A<- matrix(c(10,1,2,5,7,6,9,2,3),nrow = 3)
B<- matrix(c(11,6,8,7,3,12,3,5,9),nrow = 3)
print('Matrix A: ');print(A)
print('Matrix B: ');print(B)
# Sum of Matrices
print("Sum of matrices: ");print(A + B)
# Difference of matrices
print("Difference of Matrices: ");print(A - B)
# Determinant of Matrices
print("Determinant of marix A: ");print(det(A))
print("Determinant of marix B: ");print(det(B))
# Matrix Multiplication
print("Matrix Multiplication A X B: ");print(A%*%B)
# Corrosponding element Multiplication
print("Corrosponding element Multiplication a(i,j)*b(i,j)");print(A*B)
# Transpose of matrices
print("Transpose of Matrix A and B resectively");print(t(A));print(t(B))
# Inverse of Matrices
# install.packages('matlib')
# Determinant should not be zero for existance of inverse
library('matlib')
print("Inverse of Matrix A and B resectively");print(inv(A));print( inv(B))