import collections


class BST:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BST(data)

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BST(data)

    def in_order(self):
        ele = []
        if self.left:
            ele += self.left.in_order()

        ele.append(self.data)

        if self.right:
            ele += self.right.in_order()
        return ele


def total_internal_nodes(root):
    if root is None or (root.left is None and root.right is None):
        return 0
    else:
        return total_internal_nodes(root.left) + total_internal_nodes(root.right) + 1


def total_external_nodes(root):
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return 1
    else:
        return total_external_nodes(root.left) + total_external_nodes(root.right) + 1


def count_nodes(root):
    if root is None:
        return 0
    else:
        return count_nodes(root.left) + count_nodes(root.right) + 1


def right_view(root):
    if root is None:
        return
    q = collections.deque()
    q.append(root)

    while q:
        n = len(q)
        while n > 0:
            n -= 1
            node = q.popleft()
            if n == 0:
                print(node.data, end=" ")

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)


def build_tree():
    elements = [28, 15, 13, 25, 23, 88, 63, 10, 2]
    root = BST(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root


if __name__ == "__main__":
    root1 = build_tree()
    root1.in_order()
    right_view(root1)
    print("\n")
    print(count_nodes(root1))
    print(total_external_nodes(root1))
    print(total_internal_nodes(root1))
