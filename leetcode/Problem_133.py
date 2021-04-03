"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # clone graph using BFS ? 
        def helper(q, res):
            if not q:
                return
            
            curr = q.pop(0)
            
            for u in curr.neighbors:
                if not u.val in res:
                    res[u.val] = Node(u.val)
                    q.append(u)
                res[curr.val].neighbors.append(res[u.val])
           
            helper(q, res)
            
        q = []
        res = {}
        q.append(node)
        res[node.val] = Node(node.val)
        helper(q, res)
        return res[node.val]
