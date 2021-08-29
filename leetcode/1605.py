class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows = len(rowSum)
        cols = len(colSum)
        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                curr_val = min(rowSum[i], colSum[j])
                row.append(curr_val)
                rowSum[i] -= curr_val
                colSum[j] -= curr_val
            matrix.append(row)
        #print(matrix)
        return matrix
                
