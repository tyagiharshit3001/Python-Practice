# single Linked List
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def ins_beg(self, data):
        if self.head is None:
            self.head = Node(data, None)
        else:
            node = Node(data, self.head)
            self.head = node

    def ins_end(self, data):
        if self.head is None:
            self.ins_beg(data)
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data, None)

    def display(self):
        itr = self.head
        lis = "Head-->"
        while itr:
            lis += str(itr.data) + "-->"
            itr = itr.next
        lis += "Tail"

        print(lis)

    def reverse(self, k):
        itr = self.head
        arr = []
        while itr:
            arr.append(itr.data)
            itr = itr.next
        for j in range(len(arr)):
            if j % k != 0:
                l1 = arr[:k]
                l2 = arr[k:]
                l1.reverse()
                l2.reverse()
                arr = l1 + l2

        itr = self.head
        while itr:
            itr.data = arr.pop()
            itr = itr.next

    def one_rotation(self):
        itr = self.head
        while itr.next.next:
            itr = itr.next
        self.head = Node(itr.next.data, self.head)
        itr.next = None

    def add_1(self):

        a = 0
        lis = []
        length = 0
        itr = self.head
        while itr:
            a = a * 10 + itr.data
            itr = itr.next
            length += 1
        a += 1
        print(a)
        while a:
            lis.insert(0, a % 10)
            a = a // 10
        print(lis)
        itr = self.head
        i = 0
        while itr:
            itr.data = lis[i]
            itr = itr.next
            i += 1

        itr = self.head
        while itr.next:
            itr = itr.next

        while length < len(lis):
            itr.next = Node(lis[i], None)
            itr = itr.next
            length += 1
            i += 1

    def remove_replicas(self):
        itr = self.head
        lis = []
        while itr:
            lis.append(itr.data)
            itr = itr.next
        lis = set(lis)
        lis = sorted(list(lis))
        itr = self.head
        for i in lis:
            itr.data = i
            itr = itr.next
        itr = self.head
        count = 0
        while count != len(lis) - 1:
            itr = itr.next
            count += 1
        itr.next = None

    def remove_replica2(self):
        lis = []
        itr = self.head
        while itr:
            if itr.data not in lis:
                lis.append(itr.data)
            itr = itr.next
        itr = self.head
        temp = None
        for i in lis:
            temp = itr
            itr.data = i
            itr = itr.next
        temp.next = None






def add_nums(l1, l2):
    h1 = l1.head
    h2 = l2.head
    a = 0
    lis = []
    length1 = 0
    itr1 = h1
    while itr1:
        a = a * 10 + itr1.data
        itr1 = itr1.next
        length1 += 1

    b = 0
    length2 = 0
    itr2 = h2
    while itr2:
        b = b * 10 + itr2.data
        itr2 = itr2.next
        length2 += 1

    a += b
    while a:
        lis.insert(0, a % 10)
        a = a // 10
    print(a, lis)
    l1.head = None
    for i in lis:
        l1.ins_end(i)


if __name__ == "__main__":
    l1 = LinkedList()
    l1.ins_end(5)
    l1.ins_end(2)
    l1.ins_end(2)
    l1.ins_end(4)
    l1.display()
    l1.remove_replica2()
    l1.display()
