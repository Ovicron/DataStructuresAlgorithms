# Stack data structure
# Last in first out

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return self.items == []

    def __len__(self):
        return len(self.items)


s = Stack()

s.push(123)
s.push('abc')

print(s.items)
print(s.is_empty())
print(s.peek())
