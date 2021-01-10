
class Node:
    def __init__(self, data=None):
        self.data = dat
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    @staticmethod
    def insert_after(prev_node, val):
        if not prev_node:
            return
        new_node = Node(val)
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    # no duplicate nodes in our Linked List
    def delete_node_with_key(self, key):
        curr_node = self.head
        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return

        prev_node = None
        while curr_node and curr_node.data != key:
            prev_node = curr_node
            curr_node = curr_node.next

        if not curr_node:
            print('No element found with the given key.')
        else:
            prev_node.next = curr_node.next
            curr_node = None
    
    # no duplicate nodes in our Linked List
    def delete_node_at_pos(self, pos):
        curr_node = self.head
        if pos == 0:
            self.head = curr_node.next
            curr_node = None
            return

        prev_node = None
        count = 0
        while curr_node and count != pos:
            prev_node = curr_node
            curr_node = curr_node.next
            count += 1

        if not curr_node:
            print('No position found at the given number.')
        else:
            prev_node.next = curr_node.next
            curr_node = None

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

    def count_nodes(self):
        curr_node = self.head
        count = 0
        while curr_node:
            count += 1
            curr_node = curr_node.next
        return count


ll = LinkedList()

ll.append(1)
ll.append(2)
ll.append(3)

ll.prepend('C')
ll.prepend('B')
ll.prepend('A')

ll.insert_after(ll.head.next.next.next, 'Inserted after 1')
ll.delete_node_with_key('Inserted after 1')
ll.delete_node_at_pos(5)

ll.print_list()

print(f"There are {ll.count_nodes()} nodes in this linked list.")


