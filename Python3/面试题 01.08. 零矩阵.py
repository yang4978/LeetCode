class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_row = 0

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i == 0:
                        zero_row = 1
                    else:
                        matrix[i][0] = 0

        for i in range(1,m):
            if matrix[i][0] == 0:
                for j in range(1,n):
                    matrix[i][j] = 0


        for j in range(n):
            if matrix[0][j] == 0:
                for i in range(1,m):
                    matrix[i][j] = 0
        
        if zero_row:
            for j in range(n):
                matrix[0][j] = 0

        # row = set()
        # col = set()

        # m = len(matrix)
        # n = len(matrix[0])

        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             row.add(i)
        #             col.add(j)
        
        # for i in row:
        #     for j in range(n):
        #         matrix[i][j] = 0
        
        # for i in range(m):
        #     for j in col:
        #         matrix[i][j] = 0
