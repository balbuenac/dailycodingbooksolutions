class WordFilter:

    suffix = {}
    prefix = {}
    
    def __init__(self, words: List[str]):
        
        self.suffix = {}
        self.prefix = {}
        
        for i, w in enumerate(words):
            res = []
            l_w = list(w)
            for c in l_w:
                res.append(c)
                
                key = ''.join(res)
                if not key in self.prefix:
                    self.prefix[key] = []
                #print(key, self.prefix[key])
                self.prefix[key].insert(0, i)
                
                
        
        for i, w in enumerate(words):
            res = []
            l_w = list(w)[::-1]
            #print(l_w)
            for c in l_w:
                res.insert(0, c)
                
                key_suffix = ''.join(res)
                #print(key_suffix)
                if not key_suffix in self.suffix:
                    self.suffix[key_suffix] = []
                self.suffix[key_suffix].insert(0, i)
                
        #print(self.prefix, self.suffix)

    def f(self, prefix: str, suffix: str) -> int:
        left = None
        if prefix in self.prefix:
            left = self.prefix[prefix]
        
        right = None
        if suffix in self.suffix:
            right = self.suffix[suffix]
        
        #print(left, right, self.prefix, self.suffix[suffix])
        if left is None or right is None:
            return -1
        
        result = -1
        for i in left:
            for j in right:
                if i == j:
                    result = i
                    break
            if result > 0:
                break
        
        return result


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
