def med(day, arr):
    if day % 2 != 0:
        mid = arr[int(day / 2)]
    else:
        mid = (arr[int(day / 2) - 1] + arr[int(day / 2)])
    return mid


expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
d = 5
n = len(expenditure)
dayTrial = []
count = 0
for j in range(d, n):
    dayTrial.clear()
    dayTrial = expenditure[j-d:j]
    dayTrial.sort()

    if expenditure[j] >= 2 * med(d, dayTrial):
        count += 1

print(count)
