# Takes in a node and calculates its height from the bottom to the node itself. 
def height(self, node):
    if node is None:
        return -1
    left_height = self.height(node.left)
    right_height = self.height(node.right)
    return 1 + max(left_height, right_height)

# Using stack to keep track of each node count.
def size(self):
    if self.root is None:
        return 0

    stack = Stack()
    stack.push(self.root)
    count = 0
    while len(stack) > 0:
        node = stack.pop()
        if node.left:
            stack.push(node.left)
        if node.right:
            stack.push(node.right)
        count += 1
    return count
