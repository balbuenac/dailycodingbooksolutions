class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # sliding window !
        s = 0
        arr = []
        res = sys.maxsize
        for i in range(0, len(nums)):
            s += nums[i]
            arr.append(nums[i])
            #print(s, arr)
            if s >= target:
                while s >= target:
                    res = min(res, len(arr))
                    curr = arr.pop(0)
                    s -= curr
        if res == sys.maxsize:
            return 0
        return res
