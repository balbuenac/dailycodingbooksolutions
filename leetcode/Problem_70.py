class Solution:
    def __init__(self):
        self.count = 0
    
    def climbStairs(self, n: int) -> int:
        def helper(n, dp):
            if n < 0:
                return 0
            if n == 0:
                return 1
            if n in dp:
                return dp[n]
            dp[n-1] = helper(n-1, dp)
            dp[n-2] = helper(n-2, dp)
            dp[n] = dp[n-1] + dp[n-2] 
            return dp[n]
        
        dp = {}
        dp[0] = 1
        return helper(n, dp)
       
