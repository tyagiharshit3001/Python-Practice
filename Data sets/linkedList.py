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


if __name__ == '__main__':
    ll = LinkedList()

    ll.insert_at_beginning(1)
    ll.insert_at_beginning(11)
    ll.insert_at_beginning(111)
    ll.insert_at_end(2)
    ll.insert_at_end(22)
    ll.insert_at_end(222)
    ll.insert_values(['Apple', 'Banana', 'Mango'])
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
