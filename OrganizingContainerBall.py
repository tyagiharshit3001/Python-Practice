container = [[1, 3, 1], [2, 1, 2], [3, 3, 3]]
container2 = [[0, 2, 1], [1, 1, 1], [2, 0, 0]]
list1, list2 = [], []
for i in range(len(container)):
    sum1, sum2 = 0, 0
    for j in range(len(container)):
        sum1 = sum1 + container[i][j]
        sum2 = sum2 + container[j][i]
    list1.append(sum1)
    list2.append(sum2)
    print(sum1, sum2)
print(list1, list2)
n = max(len(list1), len(list2))
for i in range(n):
    if list1[i] not in list2:
        break
    elif list1[i] in list2:
        list2.remove(list1[i])
        n -= 1

if len(list2) == 0:
    print("Possible")
else:
    print("Impossible")