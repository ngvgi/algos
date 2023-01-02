class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def add_child(self, val):
        if val == self.val:
            return

        if val < self.val:
            if self.left:
                self.left.add_child(val)
            else:
                self.left = Node(val)
        else:
            if self.right:
                self.right.add_child(val)
            else:
                self.right = Node(val)

    def in_order(self):
        nodes = []
        if self.left:
            nodes += self.left.in_order()

        nodes.append(self.val)

        if self.right:
            nodes += self.right.in_order()

        return nodes

    def pre_order(self):
        nodes = []
        nodes.append(self.val)
        if self.left:
            nodes += self.left.pre_order()

        if self.right:
            nodes += self.right.pre_order()
        return nodes

    def post_order(self):
        nodes = []
        if self.left:
            nodes += self.left.post_order()

        if self.right:
            nodes += self.right.post_order()

        nodes.append(self.val)
        return nodes

    def search(self, val):
        if self.val == val:
            return True

        if val < self.val:
            if self.left:
                return self.left.search(val)
            return False
        if val > self.val:
            if self.right:
                return self.right.search(val)
            return False

    def find_max(self):

        if self.right:
            return self.right.find_max()
        return self.val

    def find_min(self):
        if self.left:
            return self.left.find_min()
        return self.val


def build_tree(values):
    root = Node(values[0])
    for i in range(1, len(values)):
        root.add_child(values[i])

    return root


nodes = [17, 4, 1, 20, 9, 23, 18, 34]
tree = build_tree(nodes)
print(tree.post_order())
print(tree.find_max())
# print(tree.search(17))
