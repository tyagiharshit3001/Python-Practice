n = 96
count = 0
factor = []
for i in range(2, int(pow(n, 0.5) + 1)):
    if n % i == 0:
        factor.append(i)
print(factor)
