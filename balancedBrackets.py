"""
{[()]}          first s = '{[()]}'
{[(])}          second s = '{[(])}'
{{[[(())]]}}    third s ='{{[[(())]]}}'
"""


def check(s):
    list2 = []
    for i in range(len(s)):
        if len(s) % 2 != 0:
            print("NO")
        elif s[i] == '(':
            list2.append("(")
        elif s[i] == ')':
            if (len(list2)) > 0 and list2[-1] == "(":
                list2.pop()
            else:
                return -1
        elif s[i] == '{':
            list2.append('{')
        elif s[i] == '}':
            if (len(list2)) > 0 and list2[-1] == '{':
                list2.pop()
            else:
                return -1
        elif s[i] == '[':
            list2.append('[')
        elif s[i] == ']':
            if (len(list2)) > 0 and list2[-1] == '[':
                list2.pop()
            else:
                return -1

    if len(list2) == 0:
        return 0
    else:
        return -1


n = int(input())
s = []
for i in range(n):
    s.append(input())
for i in range(n):
    res = check(s[i])
    if res == -1:
        print("NO")
    else:
        print("YES")
