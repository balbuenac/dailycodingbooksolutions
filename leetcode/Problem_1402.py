class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        # chef can cook any dish in 1 unit of time
        # like-time coefficient = time[i] * satisfaction[i]
        # time[i] is time to do dish i and the previous dishes ?
        # PROB: MAXIMUM sum of coefficient that the chec can obtain
        #       after dishes preparation
        # Dishes can  be prepared in any order and some dishes can be
        # discarded to get the maximum value.
        q = sorted(satisfaction, reverse=False)
        N = len(q)
        # print(q)
        k = 1
        max_gain = -1
        for i in range(0, N):
            t = k
            i = 1
            curr = 0
            while t > 0:
                curr += q[N - i] * t
                t = t - 1
                i = i + 1
            # print(max_gain, curr)
            max_gain = max(max_gain, curr)
            k = k + 1
        return max_gain if max_gain > 0 else 0


