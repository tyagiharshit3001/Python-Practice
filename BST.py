class BST:
    def __init__(self, data):
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
        else:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BST(data)

    def in_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_traversal()

        return elements

    def pre_traversal(self):
        elements = [self.data]

        if self.left:
            elements += self.left.pre_traversal()

        if self.right:
            elements += self.right.pre_traversal()

        return elements

    def post_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_traversal()

        if self.right:
            elements += self.right.post_traversal()

        elements.append(self.data)

        return elements

    def search_val(self, val):
        if self.data == val:
            return True

        elif val > self.data:
            if self.right:
                return self.right.search_val(val)
            else:
                return False

        else:
            if self.left:
                return self.left.search_val(val)
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

    def del_val(self, val):
        if val > self.data:
            if self.right:
                self.right = self.right.del_val(val)

        elif val < self.data:
            if self.left:
                self.left = self.left.del_val(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.left
            if self.right is None:
                return self.right

            max_val = self.left.max_ele()
            self.data = max_val
            self.left = self.left.del_val(max_val)
        return self


def build_tree(elements):
    root1 = BST(elements[0])
    for i in range(1, len(elements)):
        root1.add_child(elements[i])
    return root1


if __name__ == "__main__":
    element_list = [17, 4, 1, 20, 9, 23, 18, 34]
    root = build_tree(element_list)

    print("In order - ", root.in_traversal())
    print("Pre order - ", root.pre_traversal())
    print("Post order - ", root.post_traversal())
    print("Search 40 - ", root.search_val(40))
    print("Search 30 - ", root.search_val(30))
    print("Search 100 - ", root.search_val(100))
    print("Max- ", root.max_ele())
    print("Min- ", root.min_ele())
    root.del_val(20)
    print("Delete 20 - ", root.in_traversal())
    root.del_val(9)  # prob
    print("Delete 9 - ", root.in_traversal())
    root.del_val(17)  # prob
    print("Delete 17 - ", root.in_traversal())
