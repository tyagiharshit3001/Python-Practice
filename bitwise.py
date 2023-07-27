n = int(input())
k = int(input())

a,o,x = [0],[0],[0]

for i in range(1,n):
    for j in range(i+1, n+1):
        if i&j <k:
            a.append(i&j)
        if i|j <k:
            o.append(i|j)
        if i^j <k:
            x.append(i^j)

print(max(a),max(o), max(x))
