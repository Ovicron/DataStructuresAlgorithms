def reverse(self):
    curr = self.head
    tmp = None
    while curr:
        tmp = curr.prev
        curr.prev = curr.next
        curr.next = tmp
        curr = curr.prev
    if tmp:
        self.head = tmp.prev
