import collections
arr = arr2 = [[0, 'ab'], [6, 'cd'], [0, 'ef'], [6, 'gh'], [4, 'ij'], [0, 'ab'], [6, 'cd'], [0, 'ef'], [6, 'gh'],
              [0, 'ij'], [4, 'that'], [3, 'be'], [0, 'to'], [1, 'be'], [5, 'question'], [1, 'or'], [2, 'not'],
              [4, 'is'],
              [2, 'to'], [4, 'the']]

dicto = collections.defaultdict(list)
"""n = int(input().strip())

arr = []

for _ in range(n):
    arr.append(input().rstrip().split())"""

for i in range(int(len(arr) // 2)):
    for j in range(i, int(len(arr) // 2)):
        if arr[i][0] == arr[j][0]:
            arr[i][1] = arr[i][1].replace(arr[i][1], "-")
            arr[j][1] = arr[j][1].replace(arr[j][1], "-")

for i in range(len(arr)):
    dicto[arr[i][0]].append(arr[i][1])
dicto = collections.OrderedDict(sorted(dicto.items()))
for i in range(len(dicto)):
    print(" ".join(dicto[i]), end=" ")
