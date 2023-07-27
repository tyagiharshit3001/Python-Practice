class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None)
            self.head = node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_at_position(self, data, pos):
        if pos < 0 or pos >= self.get_length():
            print("Invalid Position")
            return

        itr = self.head
        count = 0
        while count != pos - 1:
            itr = itr.next
            count += 1
        itr.next = Node(data, itr.next)

    def insert_after_value(self, val_af, data):
        itr = self.head
        flag = 0
        while itr:
            if itr.data == val_af:
                itr.next = Node(data, itr.next)
                return
            itr = itr.next
        if flag == 0:
            print("Value doesn't exist")

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_values(self, data_list):
        for data in data_list:
            self.insert_at_beginning(data)

    def delete_at_beginning(self):
        self.head = self.head.next
        return

    def delete_at_end(self):
        itr = self.head
        count = 0
        while count != self.get_length() - 2:
            itr = itr.next
            count += 1
        itr.next = None

    def delete_at_position(self, pos):
        if pos < 0 or pos >= self.get_length():
            print("Position doesn't exist.")
        else:
            itr = self.head
            count = 0
            while count != pos - 1:
                itr = itr.next
                count += 1
            itr.next = itr.next.next

    def delete_by_value(self, value):
        itr = self.head
        flag = 0
        while itr:
            if itr.next.data == value:
                itr.next = itr.next.next
                flag = 1
                break
            itr = itr.next
        if flag == 0:
            print("Value Not found")

    def print(self):
        if self.head is None:
            print("Linked List is empty.")
            return
        itr = self.head
        lst = ''
        while itr:
            lst += str(itr.data) + '--->'
            itr = itr.next

        print(lst + "Tail")

    def remove_duplicate(self):
        itr = self.head
        unique = {}
        while itr:
            if itr.data in unique:
                unique[itr.data] += 1
            else:
                unique[itr.data] = 1
            itr = itr.next

        for i in unique.keys():
            while unique[i] != 1:
                self.delete_by_value(i)
                unique[i] -= 1

    def print_item_frequency(self):
        itr = self.head
        unique = {}
        while itr:
            if itr.data in unique:
                unique[itr.data] += 1
            else:
                unique[itr.data] = 1
            itr = itr.next
        print(unique)

    def linked_sort(self):
        itr = self.head
        while itr.next:
            itr2 = itr.next
            while itr2:
                if itr.data > itr2.data:
                    temp = itr.data
                    itr.data = itr2.data
                    itr2.data = temp
                itr2 = itr2.next
            itr = itr.next

    def middle_node(self):
        a = self.get_length()

        itr = self.head
        count = 0
        temp = itr
        while count != a//2:
            temp = itr
            count += 1
            itr = itr.next
        self.head = temp.next

    def is_palindrome(self):
        itr = self.head
        num = 0
        while itr:
            num = num * 10 + itr.data
            itr = itr.next
        temp = num
        s = 0
        while num:
            s = s*10 + num % 10
            num = num // 10
        return s == temp

def merge_linked_list(l1, l2):
    itr1 = l1.head
    while itr1.next:
        itr1 = itr1.next

    itr2 = l2.head
    while itr2.next:
        itr2 = itr2.next

    l = LinkedList()
    l.insert_at_beginning(100)
    l.insert_at_beginning(200)
    l.insert_at_beginning(300)
    itr2.next = l.head
    itr1.next = l.head
    print(itr2, "\n", itr1, "\n", l.head)
    return l1, l2, l


def linear_merge(l1, l2):
    itr = l1.head

    while itr.next:
        itr = itr.next

    itr.next = l2.head


def find_merge_link(l1, l2):
    a = l1.get_length()
    b = l2.get_length()
    diff = abs(a - b)
    itr1 = l1.head
    itr2 = l2.head
    if a > b:
        while diff != 0:
            itr1 = itr1.next
            diff -= 1
    else:
        while diff != 0:
            itr2 = itr2.next
            diff -= 1

    while itr1 and itr2:
        if itr1 == itr2:
            return itr1.data
        else:
            itr1 = itr1.next
            itr2 = itr2.next


if __name__ == '__main__':
    l1 = LinkedList()
    l1.insert_at_beginning(1)
    l1.insert_at_beginning(2)
    l1.insert_at_beginning(3)
    # l1.insert_at_beginning(4)
    # l1.insert_at_beginning(5)
    # l1.insert_at_beginning(6)
    # l1.insert_at_beginning(7)
    # l1.print()
    # l1.middle_node()
    l1.print()
    print(l1.is_palindrome())
    l2 = LinkedList()
"""l2.insert_at_beginning(10)
    l2.insert_at_beginning(20)
    l2.insert_at_beginning(30)
    l2.insert_at_beginning(40)
    l2.insert_at_beginning(50)
    l2.insert_at_beginning(60)
    linear_merge(l1, l2)
    # l1.linked_sort()

    print(find_merge_link(l1, l2))"""

""" 
    ll = LinkedList()
    ll.insert_values([10, 3, 15, 2, 12, 6, 8, 20])
    ll.linked_sort()
"""
"""    l1 = LinkedList()
    l1.insert_at_beginning(1)
    l1.insert_at_beginning(2)
    l1.insert_at_beginning(3)
    l1.insert_at_beginning(4)
    l1.insert_at_beginning(5)
    l1.insert_at_beginning(6)

    l2 = LinkedList()
    l2.insert_at_beginning(10)
    l2.insert_at_beginning(20)
    l2.insert_at_beginning(30)
    l2.insert_at_beginning(40)
    l2.insert_at_beginning(50)
    l2.insert_at_beginning(60)

    la, lb, lc = merge_linked_list(l1, l2)
"""
"""ll = LinkedList()
    
    ll.insert_at_beginning(1)
    ll.insert_at_beginning(11)
    ll.insert_at_beginning(111)
    ll.insert_at_end(2)
    ll.insert_at_end(22)
    ll.insert_at_end(11)
    ll.insert_at_end(222)
    ll.insert_values(['Apple', 'Banana', 'Mango', 1, 1, 222, 3, 11, 11, 2])
    print("Length of linked list: ", ll.get_length())
    ll.print()
    ll.delete_at_position(2)
    ll.print()
    ll.delete_at_beginning()
    ll.print()
    ll.delete_at_end()
    ll.print()
    ll.insert_at_position('Cheeko', 1)
    ll.print()
    ll.delete_by_value('Cheeko')
    ll.print()
    ll.insert_after_value(1, 0)
    ll.print()
"""
"""    #qn2
    ll.print_item_frequency()
"""
""" #qn1
    ll.remove_duplicate()
    ll.print()
"""
