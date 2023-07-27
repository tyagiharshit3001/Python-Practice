n = int(input())
orderNo = [0] * n
preparation_Time = [0] * n
consumer_No = [0] * n
for i in range(n):
    orderNo[i], preparation_Time[i] = orders[i][0],orders[i][1]
order_time = [orderNo[i] + preparation_Time[i] for i in range(n)]
for i in range(n):
    consumer_No[i] = i + 1

for i in range(n):
    for j in range(i + 1, n):
        if order_time[i] > order_time[j]:
            temp = order_time[i]
            temp2 = consumer_No[i]
            order_time[i] = order_time[j]
            consumer_No[i] = consumer_No[j]
            order_time[j] = temp
            consumer_No[j] = temp2


