class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        count = 0
        h = {}
        for curr in position:
            if curr not in h:
                h[curr] = 0
            h[curr] += 1
        set_pos = set(position)
        
        count_even, count_odd = 0, 0
        for curr in set_pos:
            if curr % 2 == 0:
                count_even += h[curr]
            else:
                count_odd += h[curr]
                
        return min(count_even, count_odd)
