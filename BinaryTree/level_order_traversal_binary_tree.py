# Using a queue - https://github.com/Ovicron/DataStructuresAlgorithms/blob/main/queue_data_structure.py

@staticmethod
def level_order_traversal(start):
    if start is None:
        return
    q = Queue()
    q.enqueue(start)
    traversal = ""
    while len(q) > 0:
        traversal += f"{q.peek()} - "
        node = q.dequeue()
        if node.left:
            q.enqueue(node.left)
        if node.right:
            q.enqueue(node.right)
    return traversal
