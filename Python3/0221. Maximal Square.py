class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix == [] : return 0

        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        res = 0

        for i in range(1,m+1):
            for j in range(1,n+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
                    res = max(res,dp[i][j])
        
        return res**2

        # if matrix == []: return 0
        # m = len(matrix)
        # n = len(matrix[0])

        # dp = [[0]*n for _ in range(m)]

        # dp[0] = [int(i) for i in matrix[0]]

        # for i in range(m):
        #     dp[i][0] = int(matrix[i][0])

        # for i in range(1,m):
        #     for j in range(1,n):
        #         if matrix[i][j]=='1':
        #             dp[i][j] = 1 
        #             if dp[i-1][j-1]:
        #                 for t in range(1,dp[i-1][j-1]+1):
        #                     k = t
        #                     while(k and matrix[i-k][j]=='1' and matrix[i][j-k]=='1'):
        #                         k -= 1
        #                     dp[i][j] = max(dp[i][j],1+t) if k==0 else dp[i][j]

        # return max(max(i) for i in dp)**2

