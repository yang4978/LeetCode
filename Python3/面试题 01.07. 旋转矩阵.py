class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # n = len(matrix)
        # k = 0

        # for m in range(n,1,-2):
        #     for i in range(m-1):
        #         temp = matrix[m-1-i+k][k]
        #         matrix[m-1-i+k][k] = matrix[m-1+k][m-1-i+k]
        #         matrix[m-1+k][m-1-i+k] = matrix[i+k][m-1+k]
        #         matrix[i+k][m-1+k] = matrix[k][i+k]
        #         matrix[k][i+k] = temp

        #     k += 1

        n = len(matrix[0])

        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j] 
                
