from collections import deque

class LRUCache:
    def __init__(self, size):
        self.h = {}
        self.lru = deque()
        self.size = size

    def set(self, key, value):
        if key in self.h:
            self.h[key] = value
        else:
            if len(self.h) == self.size:
                if self.lru:
                    lru_key = self.lru.popleft()
                    del self.h[lru_key]
            self.h[key] = value

    def get(self, key):
        if key in self.h:
            self.lru.append(key)
            return self.h[key]
        return None

lru_cache = LRUCache(5)
lru_cache.set(10, 20)
lru_cache.set(11, 21)
lru_cache.set(12, 22)
lru_cache.set(13, 23)
lru_cache.set(14, 24)
print(lru_cache.get(10))
print(lru_cache.get(11))
lru_cache.set(15, 25)
print(lru_cache.get(10))
print(lru_cache.get(15))
print(lru_cache.get(11))
