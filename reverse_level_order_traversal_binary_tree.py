@staticmethod
def reverse_level_order_traversal(start):
    if start is None:
        return

    queue = Queue()
    stack = Stack()
    queue.enqueue(start)
    traversal = ""

    while len(queue) > 0:
        node = queue.dequeue()
        stack.push(node)
        if node.right:
            queue.enqueue(node.right)
        if node.left:
            queue.enqueue(node.left)

    while len(stack) > 0:
        node = stack.pop()
        traversal += f"{node.value} - "
    return traversal
