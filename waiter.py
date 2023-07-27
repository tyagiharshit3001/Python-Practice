n = 5
q = 2
plate_No = [3, 3, 4, 4, 9]


prime_list = []
a = []
b = []
temp = []
answer = []

for num in range(1, 10000):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            prime_list.append(num)

for i in range(q):
    a.clear()
    b.clear()

    current_Prime = prime_list[i]
    for j in range(len(plate_No)):
        if plate_No[j] % current_Prime == 0:
            b.append(plate_No[j])
        else:
            a.append(plate_No[j])
    #b.reverse()
    answer.extend(b)
    plate_No = a[:]
    print(a, "\t\t", b)

#a.reverse()
answer.extend(a)
print(answer)
