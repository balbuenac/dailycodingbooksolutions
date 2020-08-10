from collections import defaultdict


class SparseArray:
    def __init__(self, size):
        self.data = defaultdict(int)
        self.size = size

    def set(self, i, val):
        self.data[i] = val

    def get(self, i):
        if i < self.size:
            if i in self.data:
                return self.data[i]
            return 0
        return -1

sparse_array = SparseArray(10)
print(sparse_array.get(0))
print(sparse_array.get(1))
print(sparse_array.get(2))
print(sparse_array.get(20))
sparse_array.set(0, 10)
print(sparse_array.get(0))
print(sparse_array.get(1))