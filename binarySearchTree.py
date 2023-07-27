class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def search_val(self, val):

        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search_val(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search_val(val)
            else:
                return False

    def max_ele(self):
        if self.right is None:
            return self.data
        return self.right.max_ele()

    def min_ele(self):
        if self.left is None:
            return self.data
        return self.left.min_ele()

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def preorder_traversal(self):
        elements = [self.data]

        if self.left:
            elements += self.left.preorder_traversal()

        if self.right:
            elements += self.right.preorder_traversal()

        return elements

    def postorder_traversal(self):

        elements = []

        if self.left:
            elements += self.left.postorder_traversal()

        if self.right:
            elements += self.right.postorder_traversal()

        elements.append(self.data)

        return elements

    def delete(self, val):
        if val > self.data:
            if self.right:
                self.right = self.right.delete(val)

        elif val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        else:
            if self.right is None and self.left is None:
                return None
            if self.right is None:
                return self.right
            if self.left is None:
                return self.left

            min_val = self.right.min_ele()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self


def build_tree(elements):
    root = BinarySearchTree(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == "__main__":
    element_list = [50, 20, 30, 40, 10, 60, 70, 80, 90]
    root = build_tree(element_list)
    print(root.preorder_traversal())
    print(root.in_order_traversal())
    print(root.postorder_traversal())
    print(root.search_val(13))
    print(root.max_ele())
    print(root.min_ele())
    root.delete(50)
    print(root.in_order_traversal())
    root.delete(60)
    print(root.in_order_traversal())
    root.delete(100)
    print(root.in_order_traversal())
