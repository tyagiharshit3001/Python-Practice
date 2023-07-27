arr = [2, -1, 2, 3, 4, -5]
sum1 = []
sum2 = []
s = 0

for i in range(len(arr)):
    if s + arr[i] > s:
        s = s + arr[i]
        sum1.append(s)
sum1 = sum1 + arr
for j in range(len(arr)):
    s2 = 0
    for k in range(len(arr)):
        s2 = s2 + arr[k]
        sum2.append(s2)

print(max(sum1), max(sum2))
