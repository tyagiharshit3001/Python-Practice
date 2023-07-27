"""
        *________*
        **      **
        ***    ***
        ****  ****
        **********

n = 10
m = int(n / 2)
for l in range(m):
    for i in range(0, l + 1):
        print("* ", end="")
    for i in range(1, n - i-l-1):
        print("  ", end="")
    for i in range(0, l + 1):
        print("* ", end="")
    print("\r")

"""

"""
        **********
        ****  ****
        ***    ***
        **      **
        *--------*
        **      **
        ***    ***
        ****  ****
        **********


n = 10
m = int(n / 2)
count = n
for l in range(m, 0, -1):
    for a in range(l, 0, -1):
        print("* ", end="")
    for i in range(0, n - 2 * l, 1):
        print("  ", end="")
    for a in range(l, 0, -1):
        print("* ", end="")
    print("\r")


for l in range(m):
    for i in range(0, l + 1):
        print("* ", end="")
    for i in range(1, n - i-l-1):
        print("  ", end="")
    for i in range(0, l + 1):
        print("* ", end="")
    print("\r")
    

    *         * 
   * *       * * 
  * * *     * * * 
 * * * *   * * * * 
* * * * * * * * * *


n = 10
m = int(n / 2)
for l in range(m):
    for i in range(m-1, l, -1):
        print(" ", end="")
    for i in range(0, l + 1):
        print("* ", end="")
    for i in range(1, n - i-l-1):
        print(" ", end="")
    for i in range(0, l + 1):
        print("* ", end="")
    print("\r")

"""


n = 10
m = int(n / 2)
for l in range(m):
    for i in range(m-1, l, -1):
        print(" ", end="")
    for i in range(0, l + 1):
        print(i+1," ", end="")
    for i in range(1, n - i-l-1):
        print(" ", end="")
    print("\r")


# Meatball Problem
"""
participants = int(input("Participants: "))
dayCapacity = int(input("Day capacity: "))
meatballWeight = []

for j in range(participants):
    meatballWeight.append(int(input()))

mbwCopy = meatballWeight

for j in meatballWeight:
    if j < dayCapacity:
        meatballWeight.remove(j)

for j in range(len(meatballWeight)):
    for i in range(len(meatballWeight)):
        m = max(meatballWeight)
        if meatballWeight[i] == m:
            meatballWeight[i] = meatballWeight[i] - dayCapacity * (participants - 1)
            for k in range(len(meatballWeight)):
                if meatballWeight[k] != meatballWeight[i] and meatballWeight[k] != min(mbwCopy) and meatballWeight[k] != max(mbwCopy):
                    meatballWeight[k] = meatballWeight[k] + (dayCapacity * (participants - 1))/(len(meatballWeight) - 2)
            

n = int(input())
m = 0
mxPos = 0
v = [0] * n
x = int(input())
for i in range(n):
    v[i] = int(input())

for i in range(n):
    v[i] = (v[i] - 1) // x
for i in range(n):
    if v[i] >= m:
        m = v[i]
        mxPos = i

print(mxPos + 1)
"""

# books problem

"""
booksNo = int(input())
earning = []
booksCost = []

for i in range(booksNo):
    earning.append(int(input()))

for i in range(booksNo):
    booksCost.append(int(input()))

totalEarn = 0
totalCost = 0

for i in range(booksNo):
    totalCost = totalCost + booksCost[i]
    totalEarn = totalEarn + earning[i]

print(totalCost - totalEarn)"""

# Homeless Homies
"""
peopleNo = int(input())
peopleHeight = []
homeCapacity = []
allocation = [0] * peopleNo

for i in range(peopleNo):
    peopleHeight.append(int(input()))

for i in range(peopleNo):
    homeCapacity.append(int(input()))

print("People: ", peopleNo)
print("People height: ", peopleHeight)
print("Home Capacity: ", homeCapacity)
count = 0
for i in range(peopleNo):
    for j in range(peopleNo):
        if homeCapacity[j] > peopleHeight[i]:
            count += 1
            homeCapacity[j] = -1
            break

print("Homeless: ", peopleNo - count)
"""

# Airport luggage Problem
"""
n = int(input())
weights = []

for i in range(n):
    weights.append(int(input()))
    
t = int(input())
cost = 0

for i in range(n):
    if weights[i] <= t:
        cost = cost + 1
    else:
        cost = cost + 2

print(cost)
"""

# 12 Hr To 24 Hr time format
"""
s = '12:45:55PM'

if s[-2] == "P" and int(s[:2]) < 12:
    h = int(s[:2])
    m = s[3:5]
    s1 = s[6:8]
    h += 12
    s2 = str(h) + ":" + m + ":" + s1
else:

    s2 = s[:len(s)-2]

if s[-2] == "A" and int(s[:2]) == 12:
    h = int(s[:2])
    m = s[3:5]
    s1 = s[6:8]
    h = str("00")
    s2 = str(h) + ":" + m + ":" + s1
else:
    s2 = s[:len(s)-2]
print(s2)"""

# junk pair sum of pair differences
"""arr = input().split(",")
arr = [int(i) for i in arr]
orderpairs = []

for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)):
        if arr[i] != arr[j] and [arr[i], arr[j]] not in orderpairs:
            orderpairs.append([arr[i], arr[j]])

diffe = [orderpairs[i][1] - orderpairs[i][0] for i in range(len(orderpairs))]
sum_of_diffes = diffe[:]

for i in range(len(diffe) - 1):
    for j in range(i + 1, len(diffe)):
        sum_of_diffes.append((diffe[i] + diffe[j]))

print(orderpairs, "\n", diffe)
print(max(sum_of_diffes))
"""

# String rotation and even consonants
"""
def rotate(input, d):
    # slice string in two parts for left and right
    Lfirst = input[0: d]
    Lsecond = input[d:]
    Rfirst = input[0: len(input) - d]
    Rsecond = input[len(input) - d:]

    return (Rsecond + Rfirst)


def sort(alpst, p):
    for k in range(1, p):
        temp = alpst[k]

        l = k - 1
        while l >= 0 and len(temp) < len(alpst[l]):
            alpst[l + 1] = alpst[l]
            l -= 1

        alpst[l + 1] = temp


n = int(input())
strings = [0] * n
d = [0] * n
vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

for i in range(n):
    strings[i], d[i] = input().split(",")
d = [int(i) for i in d]

ans = []

for j in range(n):
    s = rotate(strings[j], d[j])
    print(s)
    out = ""
    for i in range(len(s)):
        if i % 2 != 0 and s[i] not in vowel:
            out = out + s[i]
    ans.append(out)

p = len(ans)

sort(ans, p)

sorted(ans)
ans.remove("")
print(ans)"""

# Ceaser Cipher
"""
def str_rotate_right(strings, d):
    d = d % 26
    left_Part = strings[:d]
    right_Part = strings[d:]

    return right_Part + left_Part


alphas = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12,
          "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24,
          "z": 25}

alphaString = "abcdefghijklmnopqrstuvwxyz"

s = "Pz-/aI/J`EvfthGH"
k = 66

rstr = str_rotate_right(alphaString, k)

res = ""
for i in range(len(s)):
    if s[i].isalpha():
        if s[i] in alphaString:
            res = res + rstr[alphas[s[i].lower()]]
        elif s[i] in alphaString.upper():
            res = res + rstr[alphas[s[i].lower()]].capitalize()
    else:
        res = res + s[i]

print(res)
"""

"""s = "OOSDSSOSOSWEWSOSOSOSOSOSOSSSSOSOSOSS"

"OOSDSSOSOSWEWSOSOSOSOSOSOSSSSOSOSOSS"

count = 0
count_S = 0
for i in range(len(s) - 3):
    a = s[i:i + 3]
    if a[0] != "S" or a[1] != "O" or a[2] != "S":
        count += 1

print(count)
"""

"""
a, z, p = input().split(','),[],[]
a.sort(key = len)
n = [len(x) for x in a]
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if (n[j] == 2 * n[i]): z.append(a[i], a[j])
if not z: print(-1); quit()
for x,k in z:
    for y in x:
        if  y in k : p.append(y)

if p: print(*sorted(p), sep=",")
else: print(-1)



inarr = list(map(int, input().split(",")))
"""
"""

def jump(inarr):
    i = len(inarr)
    s = [-1] * i

    x = [0] * i
    x[i - 1] = 0
    x[i - 2] = 1
    s[i - 1] = i - 1
    s[i - 2] = i - 2
    i -= 3
    while i > -1:
        if inarr[i] == 0:
            x[i] = 10 ** 4 + 1
            i -= 1
            continue
        l = i + 1 + inarr[i]
        x[i] = min(x[i + 1:l]) + 1
        if x[i] == x[i - 1]:
            s[i - 1] = -1
            s[i] = i
        elif x[i] != x[i - 1]:
            s[i] = i
        i -= 1
    sum_var = 0
    for j in s:
        if j >= 0:
            sum_var += inarr[j]
    print(sum_var, x[0], sep=",")



def jump(input_array):
    i = len(input_array)

    x = [0] * i
    s = [-1] * i
    x[i - 1] = 0
    x[i - 2] = 1
    s[i - 1] = i - 1
    s[i - 2] = i - 2
    i -= 3
    while i > -1:
        if input_array[i] == 0:
            x[i] = 10 ** 4 + 1
            i -= 1
            continue
        l = i + 1 + input_array[i]
        x[i] = min(x[i + 1:l]) + 1
        if x[i] == x[i - 1]:
            s[i - 1] = -1
            s[i] = i
        elif x[i] != x[i - 1]:
            s[i] = i
        i -= 1
    sum_var = 0
    for j in s:
        if j >= 0:
            sum_var += input_array[j]
    print(x[0], sum_var)
jump(inarr)
"""

"""
n = int(input())
arr = list(map(int, input().split(" ")))


def palindrome(d):
    sum1 = 0
    while d > 0:
        a = d % 10
        sum1 = sum1 * 10 + a
        d = d // 10

    if sum1 == d:
        return True
    else:
        return False

"""
"""
if all(i >= 0 for i in arr) and any(palindrome(i) for i in arr):
    print(True)
else:
    print(False)
"""

