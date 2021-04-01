class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        subsets.append([])
        for num in nums:
            n = len(subsets)
            for i in range(n):
                currset = list(subsets[i])
                currset.append(num)
                subsets.append(currset)
        return subsets
