class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        def print_borders(matrix, output):
            
            if len(matrix) == 0 or len(matrix[0]) == 0:
                return output
            rows = len(matrix)
            cols = len(matrix[0])
            if rows == 1:
                output.extend(matrix[0])
                return output
            elif cols == 1:
                for i in range(rows):
                    output.append(matrix[i][0])
                return output
            else:
                output.extend(matrix[0])

                for i in range(1, rows-1):
                    output.append(matrix[i][-1])

                output.extend(matrix[-1][::-1])

                for i in range(1, rows-1):
                    output.append(matrix[rows-i-1][0])
                
                smaller_matrix = [row[1:-1] for row in matrix[1:-1]]
                return print_borders(smaller_matrix, output)
        
        return print_borders(matrix, output)
        

            

        