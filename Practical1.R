a <- scan()
print(max(a))
print(min(a))
print(sum(a))
print(mean(a))
print(sqrt(a))
print(round(a))


n = as.integer(readline("Enter number of rows or columen: "))
print("Enter Matrix A")
m1 = matrix(scan(), nrow = n, ncol = n, byrow = T)
print("Enter Matrix B")
m2 = matrix(scan(), nrow = n, ncol = n, byrow = T)
m3 = matrix(nrow = n, ncol = n, byrow = T)

print(m1, m2)

sum = 0
for (i in 1:n){
  for (j in 1:n){
    for (k in 1:n){
      sum = sum + m1[i,k] * m2[k,j]
    }
    m3[i,j] = sum
    sum = 0
  }
}

print(m3)

