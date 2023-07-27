class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
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

    def print_tree_only_name(self):
        prefix = " " * self.get_level() * 5 + "|--" if self.parent else ""
        print(prefix + self.name)
        for child in self.children:
            child.print_tree_only_name()

    def print_tree_only_designation(self):
        prefix = " " * self.get_level() * 5 + "|--" if self.parent else ""
        print(prefix + self.designation)
        for child in self.children:
            child.print_tree_only_designation()

    def print_tree_only_both(self):
        prefix = " " * self.get_level() * 5 + "|--" if self.parent else ""
        print(prefix + self.name + " " + self.designation)
        for child in self.children:
            child.print_tree_only_both()


def build_tree():
    root = TreeNode("Nipul", "CEO")
    return root


if __name__ == "__main__":
    root = build_tree()

    cto = TreeNode("Chinmey", "CTO")
    infra_head = TreeNode("Vishwa ", "Infrastructure Head")
    infra_head.add_child(TreeNode("Dhaval ", "Cloud Manager"))
    infra_head.add_child(TreeNode("Abhijit", " Application Manager"))
    app_head = TreeNode("Amir", " Application Head")

    hr = TreeNode("Gels ", "HR Head")
    hr.add_child(TreeNode("Peter", " Recruitment manager"))
    hr.add_child(TreeNode("Waqas", " Policy manager"))

    root.add_child(cto)
    root.add_child(hr)
    cto.add_child(infra_head)
    cto.add_child(app_head)

    print("[1]-----> To print Name Hierarchy")
    print("[2]-----> To print Designation Hierarchy")
    print("[1]-----> To print Name with Designation Hierarchy")
    opt = int(input("Enter Option: "))

    if opt == 1:
        root.print_tree_only_name()
    elif opt == 2:
        root.print_tree_only_designation()
    elif opt == 3:
        root.print_tree_only_both()
