def pairs_with_sum(self, val):
    pairs = []
    p = self.head
    q = None
    while p:
        q = p.next
        while q:
            if p.data + q.data == val:
                pairs.append(f"{p.data}, {q.data}")
            q = q.next
        p = p.next
    return pairs
