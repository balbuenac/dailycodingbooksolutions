class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # looks like we need to maximum something based on the coins we have
        # [1,6,3,1,2,5] 1, 1, 2, 3, 5, 6
        # Greedy ?
        costs.sort()
        res, count = [], 0
        for i in range(0, len(costs)):
            if costs[i] > coins:
                break
            count += 1
            coins -= costs[i]
        return count
