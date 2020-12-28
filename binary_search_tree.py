class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, val):
        if val <= self.data:
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = Node(val)
            else:
                self.right.insert(val)

    def find(self, val):
        if val == self.data:
            return True
        elif val < self.data:
            if self.left is None:
                return False
            else:
                return self.left.find(val)
        else:
            if self.right is None:
                return False
            else:
                return self.right.find(val)

    def print_in_order(self):
        if self.left is not None:
            self.left.print_in_order()
        print(self.data)
        if self.right is not None:
            self.right.print_in_order()


def search(node, key):
    if node is None or node.data == key:
        return node

    if key > node.data:
        search(node.right, key)

    return search(node.left, key)


n = Node(10)

n.insert(55)
n.insert(8)
n.insert(5)
n.insert(4)
n.insert(75)

print(n.print_in_order())
