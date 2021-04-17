class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def helper(board, i, j, m, n, word, pos, visited, prev):
            if word == prev:
                return True

            if i<0 or i>=m:
                return

            if j<0 or j>=n:
                return

            if pos >= len(word):
                return

            if board[i][j] != word[pos]:
                return False

            if not (i,j) in visited:
                visited[(i,j)] = False

            if visited[(i,j)] == True:
                return

            visited[(i,j)] = True

            prev = prev + word[pos]
            if  (helper(board,i-1,j,m,n,word,pos+1, visited, prev) or \
                        helper(board,i+1,j,m,n,word,pos+1, visited, prev) or \
                        helper(board,i,j-1,m,n,word,pos+1, visited, prev) or \
                        helper(board,i,j+1,m,n,wod,pos+1, visited, prev)):
                return True

            visited[(i,j)] = False

            return False

        m = len(board)
        n = len(board[0])
        for i in range(0, m):
            for j in range(0, n):
                if board[i][j] == word[0]:
                    visited = {}
                    visited[(i,j)] = False
                    if (helper(board, i, j, m, n, word, 0, visited,"")):
                        return True
        return Falser
