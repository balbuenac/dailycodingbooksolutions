class Solution:
    def __init__(self):
        self.result = []

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def helper(i, g, v, N, arr):
            v[i] = True
            arr.append(i)

            if i == N-1:
                self.result.append(arr.copy())
            else:
                for curr in g[i]:
                    if v[curr] == False:
                        helper(curr, g, v, N, arr)

            v[i] = False
            arr.remove(i)

        v = {i:False for i in range(0, len(graph))}
        helper(0, graph, v, len(graph), [])
        return self.result


