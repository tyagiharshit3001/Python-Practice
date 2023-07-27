n = 5
m = 2
s = 2

list1 = [i+1 for i in range(n)]

leftPart = list1[:s-1]
rightPart = list1[s-1:]

list2 = rightPart + leftPart

a = m % n

print(list2[a - 1])

