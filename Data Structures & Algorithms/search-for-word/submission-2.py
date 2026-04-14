class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i, visited):
            if r == rows or c == cols or c == -1 or r == -1 or [r, c] in visited:
                return False
            if board[r][c] == word[i]:
                if i == len(word)-1:
                    return True
                else:
                    visited.append([r, c])
                    left = dfs(r, c-1, i+1, visited)
                    right = dfs(r, c+1, i+1, visited)
                    top = dfs(r-1, c, i+1, visited)
                    bottom = dfs(r+1, c, i+1, visited)
                    visited.pop(-1)
                    return left or right or top or bottom
            else:
                return False
        visited = []
        for i in range(rows):
            for j in range(cols):
                print(board[i][j])
                if dfs(i, j, 0, []):
                    return True
        return False
                    
                    

