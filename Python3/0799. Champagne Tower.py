class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        matrix = [[0]*(101) for _ in range(101)]
        matrix[0][0] = poured

        for i in range(query_row+1):
            for j in range(query_row+1):
                if matrix[i][j]>1:
                    matrix[i+1][j] += (matrix[i][j]-1)/2
                    matrix[i+1][j+1] +=  (matrix[i][j]-1)/2
                    matrix[i][j] = 1
        return matrix[query_row][query_glass]
