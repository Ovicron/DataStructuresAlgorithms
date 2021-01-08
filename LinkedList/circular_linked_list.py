
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        curr = self.head
        new_node.next = self.head
        if not self.head:
            new_node.next = new_node
        else:
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
        self.head = new_node

    def remove_node(self, key):
        if not self.head:
            return

        if self.head.data == key:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = self.head.next
            self.head = self.head.next
        else:
            prev = None
            curr = self.head
            while curr.next != self.head:
                prev = curr
                curr = curr.next
                if curr.data == key:
                    prev.next = curr.next

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
            if curr == self.head:
                return

    @staticmethod
    def is_circular(input_list):
        curr = input_list.head
        while curr.next:
            curr = curr.next
            if curr.next == input_list.head:
                return True
        return False


cll = CircularLinkedList()

cll.append(1)
cll.append(2)
cll.append(3)
cll.remove_node(3)
cll.print_list()
print(cll.is_circular(cll))
