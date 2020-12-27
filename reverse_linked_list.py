def reverse_list(self):
    prev = None
    curr = self.head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    self.head = prev
