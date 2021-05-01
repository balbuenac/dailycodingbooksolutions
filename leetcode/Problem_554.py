class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # minimun number of crossed bricks
        # 2D array wall => = O(n) o O(logn)
        h = {}
        rows, cols = len(wall), 0
        total_row = sum(wall[0])
        
        for row in range(0, rows):
            curr_sum = 0
            cols = len(wall[row])
            for col in range(0, cols-1):
                curr_sum += wall[row][col]
                if curr_sum not in h:
                    h[curr_sum] = 0
                h[curr_sum] += 1
        
        if len(h) == 0:
            return rows
        
        max_v = -1
        for k, v in h.items():
            max_v = max(max_v, v)
        
        return rows - max_v
        
