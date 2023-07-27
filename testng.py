'''
x = 100

list1 = [1] * (x + 1)
for i in range(2, (x // 2) + 1):
    if list1[i]:
        for j in range(i + 1, x + 1):
            if j % i == 0:
                list1[j] = 0

for k in range(2, x + 1):
    if list1[k]:
        print(k, end=", ")

'''
print("hhhhhhhheeeellloooo")