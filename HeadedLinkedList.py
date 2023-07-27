class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class HeaderLinkedList:
    def __init__(self):
        self.head = None
        self.tail = Node()

    def insert_beginning(self, data):
        if self.head is None:
            node = Node(data, self.tail)
            self.head = node
        else:
            node = Node(data, self.head)
            self.head = node

    def insert_end(self, data):
        if self.head is None:
            self.insert_beginning(data)
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            node = Node(data, self.tail)
            itr.next = node


if __name__ == "__main__":
    ll = HeaderLinkedList()
    ll.insert_beginning(5)
    ll.insert_beginning(10)
    ll.insert_beginning(15)
    ll.insert_beginning(20)
    ll.insert_end(30)
