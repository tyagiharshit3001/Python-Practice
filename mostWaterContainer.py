n = int(input())
height = []

for i in range(n):
    height.append(int(input()))

max_area = 0

for i in range(n):
    for j in range(n - 1, 0, -1):
        if i < j:
            max_area = max(max_area, min(height[i], height[j]) * (j - i))
print(max_area)
