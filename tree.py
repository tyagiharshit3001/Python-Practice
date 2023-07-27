class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        prnt = self.parent
        level = 0
        while prnt:
            level += 1
            prnt = prnt.parent
        return level

    def print_tree(self):
        prefix = " " * self.get_level() * 5 + "|--" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_tree():
    root = TreeNode("Nipul CEO")
    return root


if __name__ == "__main__":
    root1 = build_tree()

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Thinkpad"))
    laptop.add_child(TreeNode("HP"))
    laptop.add_child(TreeNode("Dell"))

    mob = TreeNode("Mobiles")
    mob.add_child(TreeNode("Pixel"))
    mob.add_child(TreeNode("iPhone"))
    mob.add_child(TreeNode("Realme"))

    tv = TreeNode("Television")
    tv.add_child(TreeNode("Ramsung"))
    tv.add_child(TreeNode("One+"))
    tv.add_child(TreeNode("Whirlpool"))

    root1.add_child(laptop)
    root1.add_child(tv)
    root1.add_child(mob)

    root1.print_tree()
