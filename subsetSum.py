array1 = [1,2,3,9,5]
x = len(array1)
"""for i in range(x):
    array1.append(int(input()))"""
sum1 = []
sum2 = 0
count = 1
if x > 2:
    for i in range(0, x, 2):
        sum2 = sum2 + array1[i]
        sum1.append(sum2)
    print(max(sum1))
else:
    print("Very less elements")
