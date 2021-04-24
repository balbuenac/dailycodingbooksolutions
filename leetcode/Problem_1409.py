class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        perm = [i for i in range(1, m+1)]
        res = []
        for q in queries:
            for i in range(0, len(perm)):
                if perm[i] == q:
                    break
            res.append(i)
            temp = perm[i]
            del perm[i]
            perm.insert(0, temp)
            #print(perm)
        return res


