# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        res = -1
        q = [(root, 1)]
        count_none = 0
        while q:
            size = len(q)
            startcounting, count = False, 0
            max_curr = 0
            left, right = 0 , 0
            while size > 0:
                curr, idx = q.pop(0)
                if startcounting == False and curr:
                    left = idx
                    startcounting = True
                    
                if startcounting and curr:
                    right = idx
                    max_curr = max(max_curr, right - left + 1)
                
                if curr:
                    if curr.left:
                        q.append((curr.left, idx*2))
                    if curr.right:
                        q.append((curr.right, idx*2 + 1))
                        
                size -= 1
            res = max(res, max_curr)
        return res
        
