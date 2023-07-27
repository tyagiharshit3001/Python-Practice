"""gene = 'GAAATAAA'
dicto = {"A": 0, "G": 0, "T": 0, "C": 0}
disStr = []
count = 0
i = 0
j = len(gene)

while i < j:
    if dicto[gene[j]] < len(gene) // 4:
        j -= 1
        dicto[gene[j]] += 1
    elif dicto[gene[j]] < len(gene) //4:
        j
"""

x = int(input())
s = input()
dic = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
for i in s:
    dic[i] += 1
x = len(s)
n = x / 4
i = 0
j = 0
mine = x
if dic['A'] == n and dic['T'] == n and dic['C'] == n and dic['G'] == n:
    print(0)
else:
    while i < x and j < x:
        while (dic['A'] > n or dic['C'] > n or dic['T'] > n or dic['G'] > n) and i < x:
            dic[s[i]] -= 1
            i += 1
        while dic['A'] <= n and dic['C'] <= n and dic['T'] <= n and dic['G'] <= n:
            dic[s[j]] += 1
            j += 1
if i - j < mine:
    mine = i - j + 1
print(mine)
