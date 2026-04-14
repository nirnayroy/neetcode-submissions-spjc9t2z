class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n_row, n_col = len(board), len(board[0])


        def dfs(r, c, visited):
            if (r, c) in visited or r == -1 or r == n_row or c == -1 or c == n_col or board[r][c]=='X':
                return
            visited.add((r, c))
            dfs(r+1, c, visited)
            dfs(r, c+1, visited)
            dfs(r-1, c, visited)
            dfs(r, c-1, visited)
        
        visited = set()
        for i in range(n_row):
            dfs(i, 0, visited)
            dfs(i, n_col-1, visited)

        for i in range(n_col):
            dfs(0, i, visited)
            dfs(n_row-1, i, visited)
        
        for i in range(n_row):
            for j in range(n_col):
                if board[i][j] == 'O' and (i, j) not in visited:
                    board[i][j] = 'X'