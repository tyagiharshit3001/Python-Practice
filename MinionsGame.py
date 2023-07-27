s = "BANANA"
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
stuart = []
count = 0
kevin = []

for i in range(len(s)):
    if s[count] in vowels:
        for j in range(len(s) - count):
            kevin.append(s[count:j + count + 1])
        count += 1
    elif s[count] not in vowels:
        for j in range(len(s) - count):
            stuart.append(s[count:j + 1 + count])
        count += 1

if len(stuart) > len(kevin):
    print("Stuart ", len(stuart))
else:
    print("Kevin ", len(kevin))

print(len(stuart), len(kevin))
