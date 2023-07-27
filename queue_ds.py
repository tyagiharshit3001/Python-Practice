from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue1(self, data):
        self.queue.appendleft(data)

    def dequeue1(self):
        return self.queue.pop()

    def is_empty(self):
        return len(self.queue) == 0

    def q_size(self):
        return len(self.queue)

    def display(self):
        st = "Rear-->"
        for i in self.queue:
            st += str(i) + " | "
        st += "<--Front"
        print(st)


if __name__ == "__main__":
    q = Queue()
    print(q.is_empty())
    q.enqueue1(1)
    q.enqueue1(2)
    q.enqueue1(3)
    q.enqueue1(4)
    q.display()
    print(q.is_empty())
    print(q.dequeue1())
    print(q.dequeue1())
    print(q.dequeue1())
    q.display()
    print(q.q_size())
    print(q.is_empty())
