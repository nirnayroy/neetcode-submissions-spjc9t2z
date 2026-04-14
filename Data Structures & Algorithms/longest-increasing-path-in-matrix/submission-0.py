class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n_rows, n_cols = len(matrix), len(matrix[0])
        path_map = {}
        
        cur_max = 0
        def dfs(r, c, path_len, prev_num):
            if r == -1 or c == -1 or r == n_rows or c == n_cols or matrix[r][c] <= prev_num:
                return path_len
            elif (r, c) in path_map:
                return path_map[(r, c)]
            else:
                max_path = max(
                    dfs(r+1, c, path_len, matrix[r][c]),
                    dfs(r, c+1, path_len, matrix[r][c]),
                    dfs(r-1, c, path_len, matrix[r][c]),
                    dfs(r, c-1, path_len, matrix[r][c])
                )+1
                path_map[(r, c)] = max_path
                return max_path
        for i in range(n_rows):
            for j in range(n_cols):
                cur_max = max(cur_max, dfs(i, j, 0, -1))

        return cur_max 

            