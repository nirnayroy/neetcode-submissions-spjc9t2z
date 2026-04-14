class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n_row, n_col = len(heights), len(heights[0])
        pac_set, atl_set = set(), set()
        
        def dfs(r, c, visited, prev_height):
            if (r, c) in visited or r == -1 or r == n_row or c == -1 or c == n_col or heights[r][c]<prev_height:
                return
            visited.add((r, c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
        
        for i in range(n_row):
            dfs(i, 0, pac_set, heights[i][0])
            dfs(i, n_col-1, atl_set, heights[i][n_col-1])

        for i in range(n_col):
            dfs(0, i, pac_set, heights[0][i])
            dfs(n_row-1, i, atl_set, heights[n_row-1][i])

        res = []
        for i in range(n_row):
            for j in range(n_col):
                if (i, j) in pac_set and (i, j) in atl_set:
                    res.append([i, j])
        return res
        # for i in range(0, len(heights)):
        #     for j in range(0, len(heights)):
        #         if i == 0 or j == 0:
        #             pacific_points.append([i, j])
        #         elif i == len(heingts) or j == len(heights[0]):
        #             atlantic_points.append([i, j])
        #         elif 