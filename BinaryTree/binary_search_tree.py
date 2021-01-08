
class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print(f"'{data}' already exists in the tree.")

    def find(self, key):
        if self.root:
            found = self._find(key, self.root)
            if found:
                return True
            return False
        return None

    def _find(self, key, cur_node):
        if key == cur_node.data:
            return self.root

        if key < cur_node.data and cur_node.left:
            return self._find(key, cur_node.left)
        elif key > cur_node.data and cur_node.right:
            return self._find(key, cur_node.right)
        return False

    def in_order_traversal(self, start):
        if start.left:
            self.in_order_traversal(start.left)
        print(start.data)
        if start.right:
            self.in_order_traversal(start.right)

    def post_order_traversal(self, start):
        if start.left:
            self.post_order_traversal(start.left)
        if start.right:
            self.post_order_traversal(start.right)
        print(start.data)

    def pre_order_traversal(self, start):
        print(start.data)
        if start.left:
            self.pre_order_traversal(start.left)
        if start.right:
            self.pre_order_traversal(start.right)


tree = BinarySearchTree()
tree.insert(8)
tree.insert(3)
tree.insert(10)
tree.insert(1)
tree.insert(6)
tree.insert(14)
tree.insert(4)
tree.insert(7)
tree.insert(13)
