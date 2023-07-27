n = int(input())
shoeNo = []
shoeNo.extend(input().split())
m = int(input())
customerShoe = [0] * m
shoePrice = [0] * m
for i in range(m):
    customerShoe[i], shoePrice[i] = input().split()
shoeNo = [int(i) for i in shoeNo]
customerShoe = [int(i) for i in customerShoe]
shoePrice = [int(i) for i in shoePrice]
cost = 0
for i in range(m):
    if customerShoe[i] in shoeNo:
        cost = cost + shoePrice[i]
        shoeNo.remove(customerShoe[i])

print(cost)
