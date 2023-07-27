a = c = [4, 2, 4, 6, 1]
b = d = [2, 1, 8, 5]
maxSum = 10
sum1 = 0
listOperandCount = []
eleCountSum = []
for i in range(len(a)):
    if sum1 + c[0] <= maxSum:
        p = c.pop(0)
        listOperandCount.append(p)
        sum1 = sum1 + p
    else:
        break

eleCountSum.append(len(listOperandCount))
listOperandCount.clear()
sum1 = 0

for i in range(len(b)):
    if sum1 + d[0] <= maxSum:
        p = d.pop(0)
        listOperandCount.append(p)
        sum1 = sum1 + p
    else:
        break

eleCountSum.append(len(listOperandCount))
listOperandCount.clear()
sum1 = 0

while sum1 <= maxSum:

eleCountSum.append(len(listOperandCount))

print(sum1, eleCountSum, listOperandCount)
