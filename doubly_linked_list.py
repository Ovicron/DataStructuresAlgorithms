
class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.prev = None
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr
            new_node.next = None

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.prev = None
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def remove_key(self, key):
        curr = self.head
        while curr:
            if curr.data == key and curr == self.head:
                # Case 1
                if not curr.next:
                    curr = None
                    self.head = None
                    return

                # Case 2
                else:
                    nxt = curr.next
                    curr.next = None
                    nxt.prev = None
                    curr = None
                    self.head = nxt

            elif curr.data == key:
                # Case 3:
                if curr.next:
                    nxt = curr.next
                    prev = curr.prev
                    prev.next = nxt
                    nxt.prev = prev
                    curr.next = None
                    curr.prev = None
                    curr = None
                    return
                else:
                    # Case 4
                    prev = curr.prev
                    prev.next = None
                    curr.prev = None
                    curr = None
                    return
            curr = curr.next

    def remove_node(self, node):
        curr = self.head
        while curr:
            if curr == node and curr == self.head:
                # Case 1
                if not curr.next:
                    curr = None
                    self.head = None
                    return

                # Case 2
                else:
                    nxt = curr.next
                    curr.next = None
                    nxt.prev = None
                    curr = None
                    self.head = nxt

            elif curr == node:
                # Case 3:
                if curr.next:
                    nxt = curr.next
                    prev = curr.prev
                    prev.next = nxt
                    nxt.prev = prev
                    curr.next = None
                    curr.prev = None
                    curr = None
                    return
                else:
                    # Case 4
                    prev = curr.prev
                    prev.next = None
                    curr.prev = None
                    curr = None
                    return
            curr = curr.next

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
    
    def remove_duplicates(self):
    seen = {}
    curr = self.head
    while curr:
        if curr.data not in seen:
            seen[curr.data] = 1
            curr = curr.next
        else:
            nxt = curr.next
            self.remove_node(curr)
            curr = nxt



dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.append(5)

