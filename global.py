class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        prnt = self.parent
        while prnt:
            level += 1
            prnt = prnt.parent
        return level

    def print_tree(self, level):
        if self.get_level() <= level:
            prefix = " " * self.get_level() * 3 + "|--" if self.parent else ""
            print(prefix + self.data)
            for child in self.children:
                child.print_tree(level)


def build_tree():
    root = TreeNode("Global")
    return root


if __name__ == "__main__":
    root = build_tree()

    usa = TreeNode("USA")
    nj = TreeNode("New Jersey")
    nj.add_child(TreeNode("Princeton"))
    nj.add_child(TreeNode("Trenton"))

    clf = TreeNode("California")
    clf.add_child(TreeNode("San Francisco"))
    clf.add_child(TreeNode("Mountain View"))
    clf.add_child(TreeNode("Polo Alto"))

    ind = TreeNode("India")
    guj = TreeNode("Gujrat")
    guj.add_child(TreeNode("Ahemdabad"))
    guj.add_child(TreeNode("Baroda"))

    ktk = TreeNode("Karnatka")
    ktk.add_child(TreeNode("Bangluru"))
    ktk.add_child(TreeNode("Mysore"))

    root.add_child(usa)
    usa.add_child(clf)
    usa.add_child(nj)

    root.add_child(ind)
    ind.add_child(guj)
    ind.add_child(ktk)

    root.print_tree(int(input("Enter Level: ")))
