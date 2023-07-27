class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        if self.head is None:
            node = Node(data, self.head)
            self.head = node
            return
        node = Node(data, self.head)
        self.head = node
        if self.head is not None:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = self.head




if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.insert_beginning(5)
    cll.insert_beginning(10)
    cll.insert_beginning(15)
    cll.insert_beginning(25)
    cll.insert_beginning(35)
    cll.insert_beginning(45)
    cll.insert_beginning(55)
    # cll.print_list()
