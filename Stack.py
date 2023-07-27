from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, data):
        self.stack.append(data)

    def pops(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        return self.stack[-1]

    def get_stc_length(self):
        return len(self.stack)

    def tos(self):
        return self.get_stc_length() - 1

    def display(self):
        if len(self.stack) == 0:
            print("Empty Stack")
            return

        lst = " "
        for ele in self.stack:
            lst += str(ele) + '---'
        lst += '<---TOS'
        print(lst)

    def revstr(self):
        st = ""
        while self.get_stc_length():
            st += self.pops()
        return st


if __name__ == '__main__':
    stc = Stack()
    s1 = '("))")'
    open_bracket = ['(', '[', '{']
    close_bracket = [')', ']', '}']
    bracket = ['()', '[]', '{}']

    for i in range(0, len(s1)):
        if s1[i] in open_bracket or s1[i] in close_bracket:
            stc.push(s1[i])
        elif s1[i] in close_bracket and stc.get_stc_length() != 0 and close_bracket.index(s1[i]) == open_bracket.index(
                stc.peek()):
            stc.pops()

    if stc.get_stc_length() != 0:
        print("Unbalanced Brackets")
    else:
        print("Balanced Brackets")

"""print(stc.is_empty())
    stc.push(2)
    stc.push(22)
    stc.push(222)
    stc.push(2222)
    stc.display()
    print(stc.peek())
    print(stc.get_stc_length())
    stc.display()
    stc.pops()
    stc.pops()
    stc.display()
    print(stc.is_empty())
"""

"""

    st = '(we will conquer COVID - 19)'
    s1 = '("({a+b))")'
    s2 = '(")) ((a+b){")'
    s3 = '("((a+b))")'
    s4 = '("))")'
    s5 = '("[a+b]+(x+2y)*{gg+kk)")'
    for i in s1:
        stc.push(i)
"""
