"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix.
This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]],
target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]],
target = 13
Output: false


mat = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
tar = 13
flag = 0


def bins(matrix, low, high, target):
    if high >= low:
        mid = (low + high) // 2

        if matrix[mid] == target:
            return True

        elif target > matrix[mid]:
            return bins(matrix, mid + 1, high, target)

        else :
            return bins(matrix, low, mid - 1, target)

    else:
        return False


for i in range(len(mat)):
    lis = mat[i]
    if tar < lis[-1]:
        print(bins(lis, 0, len(lis), tar))
        break


"""
"""
p = [4, 3, 5, 1, 2]
arr = []
for i in range(len(p)):
    arr.append(p.index(p.index(i+1)+1)+1)


print(arr)"""
"""
s = 'y'
t = 'yu'
k = 2

count = 1
lis = []
lis2 = []
for i in range(len(s)):
    lis.append(s[:i + 1])

for i in range(len(t)):
    lis2.append(t[:i + 1])

count_unmatch = 0
count_unmatch2 = 0

for i in range(len(lis)):
    if lis[i] != t[:len(lis[i])]:
        count_unmatch += 1

for i in range(len(lis2)):
    if lis2[i] != s[:len(lis2[i])]:
        count_unmatch2 += 1

if count_unmatch + count_unmatch2 <= k:
    print("YES")
else:
    print("NO")
"""

arr = [1, 2, 3, 1, 2, 3, 3, 3]

dicto = {}

for i in range(len(arr)):
    if arr[i] in dicto:
        dicto[arr[i]] += 1
    else:
        dicto[arr[i]] = 1

print(max(dicto.values()))
