"""
x = int(input())
y = int(input())
z = int(input())
n = int(input())
lit = []

for i in range(0, x+1):
    for j in range(0, y+1):
        for k in range(0, z+1):
            if i + j + k != n:
                lit.append([i, j, k])

print(lit)
"""

"""
n = int(input())
arr = map(int, input().split())
brr = sorted(arr)
if n > 1:
    for i in range(1, n):
        if brr[i - 1] < brr[i]:
            runner = brr[i - 1]
else:
    runner = brr[1]

print(runner)
"""
"""
n = int(input())
nam = []
scr = []
a = []
b = []
for _ in range(n):
    name = input()
    nam.append(name)
    score = float(input())
    scr.append(score)

nam = a
scr = b

for i in range(n):
    key = b[i]
    key2 = a[i]
    j = i - 1
    while j >= 0 and key < b[j]:
        b[j + 1] = b[j]
        a[j + 1] = a[j]
        j -= 1
    b[j + 1] = key
    a[j + 1] = key2

for i in range(n):
if n > 1:
    if b[i+1] > b[i]"""







if __name__ == "__main__":
    res(10)
