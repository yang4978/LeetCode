class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # n = len(matrix)
        # k = 0
        # while(k<n//2):
        #     for times in range(n-2*k-1):
        #         temp = matrix[k][k]
        #         for j in range(k,n-k-1):
        #             temp,matrix[k][j+1] = matrix[k][j+1],temp
                
        #         for i in range(k,n-k-1):
        #             temp,matrix[i+1][n-k-1] = matrix[i+1][n-k-1],temp
                
        #         for j in range(n-k-1,k,-1):
        #             temp,matrix[n-k-1][j-1] = matrix[n-k-1][j-1],temp
                
        #         for i in range(n-k-1,k,-1):
        #             temp,matrix[i-1][k] = matrix[i-1][k],temp
        #     k += 1

        matrix[:] = map(list,zip(*matrix[::-1]))
