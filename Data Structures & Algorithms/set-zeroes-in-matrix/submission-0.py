class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        zero_rows = []
        zero_cols = []
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.append(i)
                    zero_cols.append(j)
        print(zero_cols)
        print(zero_rows)
        for i in range(rows):
            if i in zero_rows:
                matrix[i] = [0]*cols
            for j in range(cols):
                
                if j in zero_cols:
                    matrix[i][j] = 0
        
        
            