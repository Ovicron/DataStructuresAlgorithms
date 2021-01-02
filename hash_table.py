# This uses chaining to solve collisions. 

class HashTable:
    def __init__(self):
        self.max = 10
        self.arr = [[] for _ in range(self.max)]

    def get_hash(self, key):
        c = 0
        for char in key:
            c += ord(char)
        return c % self.max

    def __setitem__(self, key, value):
        h = self.get_hash(key)

        found = False
        for idx, elem in enumerate(self.arr[h]):
            if len(elem) == 2 and elem[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)

        for elem in self.arr[h]:
            if elem[0] == key:
                return elem[1]
        return None

    def __delitem__(self, key):
        h = self.get_hash(key)

        for idx, elem in enumerate(self.arr[h]):
            if elem[0] == key:
                del self.arr[h][idx]


hash_map = HashTable()

hash_map['march 6'] = 'Hi'
hash_map['march 17'] = 'Bye'
hash_map['Ger'] = 'Nick'


print(hash_map.arr)

del hash_map['march 6']

print(hash_map.arr)
