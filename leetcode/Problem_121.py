class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        N = len(prices)
        if N == 1:
            return 0
        
        buy, sell = 0, 0
        max_profit = 0
        while i < N and j < N:
            buy = prices[i]
            if prices[j] > buy:
                while j < N and prices[j] > buy:
                    sell = prices[j]
                    max_profit = max(max_profit, sell-buy)
                    j += 1
            else:
                i += 1
                j = i + 1
            
        return max_profit
