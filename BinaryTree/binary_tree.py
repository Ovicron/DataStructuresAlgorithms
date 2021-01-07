class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    # https://i.imgur.com/dXrYNNV.png - Root -> Left -> Right
    def pre_order_traversal(self, start, traversal):
        if start:
            traversal += f"{start.value} - "
            traversal = self.pre_order_traversal(start.left, traversal)
            traversal = self.pre_order_traversal(start.right, traversal)
        return traversal

    # https://i.imgur.com/VwNTEMU.png - Left -> Root -> Right
    def in_order_traversal(self, start, traversal):
        if start:
            traversal = self.in_order_traversal(start.left, traversal)
            traversal += f"{start.value} - "
            traversal = self.in_order_traversal(start.right, traversal)

        return traversal

    # https://rb.gy/wixa1u -  Left -> Right -> Root
    def post_order_traversal(self, start, traversal):
        if start:
            traversal = self.post_order_traversal(start.left, traversal)
            traversal = self.post_order_traversal(start.right, traversal)
            traversal += f"{start.value} - "
        return traversal

    def print_tree(self, traversal_type):
        traversal_type = traversal_type.lower()
        if traversal_type == 'preorder':
            return self.pre_order_traversal(self.root, "")
        elif traversal_type == 'inorder':
            return self.in_order_traversal(self.root, "")
        elif traversal_type == 'postorder':
            return self.post_order_traversal(self.root, "")
        else:
            print('Traversal type not supported')


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.right.right = Node(4)
tree.root.left.right = Node(5)
tree.root.left.left = Node(6)
tree.root.right.left = Node(7)

print(tree.print_tree("POSTORDER"))
