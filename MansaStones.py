n = 5
a = 3
b = 23
""" """
stones = [a, b]

sum2 = []
sum3 = []
for i in range(n - 1):
    sum1 = sum4 = 0
    sum1 = sum1 + a * i + b * (n - i - 1)
    sum4 = sum4 + b * i + a * (n - 1 - i)
    sum2.append(sum1)
    sum3.append(sum4)

for i in range(len(sum2)):
    if sum2[i] in sum3:
        sum3.remove(sum2[i])
list1 = sum3 + sum2
list1.sort()
print(list1)
