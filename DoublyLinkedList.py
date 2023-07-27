class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedLis:
    def __init__(self):
        self.head = None

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_beginning(self, data):
        if self.get_length() == 0:
            node = Node(None, data, None)
            self.head = node
        else:
            node = Node(None, data, self.head)
            self.head.prev = node
            self.head = node

    def insert_end(self, data):
        if self.get_length() == 0:
            node = Node(None, data, None)
            self.head = node
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            node = Node(itr, data, None)
            itr.next = node

    def insert_position(self, data, pos):
        if pos == 0:
            self.insert_at_beginning(data)
        elif pos == self.get_length():
            self.insert_end(data)
        else:
            count = 0
            itr = self.head
            while count != pos - 1:
                itr = itr.next
                count += 1
            node = Node(itr, data, itr.next)
            itr.next.prev = node
            itr.next = node

    def link_tail_to_head(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = self.head

    def del_beginning(self):
        if self.get_length():
            self.head = self.head.next
            self.head.prev = None
        else:
            print("Linked list is empty.")

    def del_end(self):
        if self.get_length():
            itr = self.head
            while itr.next.next:
                itr = itr.next
            itr.next = None
        else:
            print("Linked list is empty")

    def del_position(self, pos):
        if pos == 0:
            self.del_beginning()
        elif pos == self.get_length():
            self.del_end()
        else:
            count = 0
            itr = self.head
            while count != pos - 1:
                itr = itr.next
                count += 1

            itr.next = itr.next.next
            itr.next.prev = itr

    def display(self):
        if self.head is None:
            print("Linked List is empty.")
            return
        itr = self.head
        lst = 'Head-->'
        while itr:
            lst += str(itr.data) + '--->'
            itr = itr.next

        print(lst + "Tail")

    def is_sorted(self):
        itr = self.head
        while itr.next:
            if itr.data > itr.next.data:
                return False
            itr = itr.next
        return True


if __name__ == '__main__':
    ll = DoublyLinkedLis()
    ll.insert_at_beginning(3)
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(1)
    ll.display()
    ll.insert_end(5)
    ll.insert_end(6)
    ll.insert_end(7)
    ll.display()
    ll.insert_position(4, 3)
    ll.display()
    ll.del_beginning()
    ll.display()
    ll.del_end()
    ll.display()
    ll.del_position(2)
    ll.display()

