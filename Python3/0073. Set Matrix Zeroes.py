class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        col_zero = 0
        row_zero = 0
        for i in range(m):
            if matrix[i][0] == 0:
                col_zero = 1
                break
        
        for j in range(n):
            if matrix[0][j] == 0:
                row_zero = 1
                break
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1,m):
            if matrix[i][0] == 0:
                for j in range(1,n):
                    matrix[i][j] = 0
                
        for j in range(1,n):
            if matrix[0][j] == 0:
                for i in range(1,m):
                    matrix[i][j] = 0

        if row_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        if col_zero:
            for i in range(m):
                matrix[i][0] = 0


        # row = set()
        # col = set()
        # m = len(matrix)
        # n = len(matrix[0])

        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             row |= {i}
        #             col |= {j}
        
        # for i in range(m):
        #     for j in range(n):
        #         if i in row or j in col:
        #             matrix[i][j] = 0
        
