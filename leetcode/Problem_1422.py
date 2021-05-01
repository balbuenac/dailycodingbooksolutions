class Solution:
    def maxScore(self, s: str) -> int:
        N = len(s)
        count_left, count_right = 0, 0 
        max_count = 0
        for i in range(0, N-1):
            if s[i] == '0':
                count_left += 1
            count_right = 0
            for j in range(i+1, N):
                if s[j] == '1':
                    count_right += 1
            max_count = max(max_count, count_left + count_right)
        return max_count
            
                
