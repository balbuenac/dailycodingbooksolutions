class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def sum_digits(n):
            total = 0
            while n > 0:
                dig = n % 10
                n = n // 10
                total += dig
            return total
        result = [0] * (highLimit + 1)
        for i in range(lowLimit, highLimit+1):
            summ = sum_digits(i)
            result[summ] += 1
        return max(result)
                
            
