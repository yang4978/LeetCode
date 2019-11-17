class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if(obstacleGrid[0][0]):
            return 0
        
        obstacleGrid[0][0] = 1

        for i in range(1,m):
            obstacleGrid[i][0] = int(obstacleGrid[i-1][0] and (obstacleGrid[i][0]==0))
        
        for j in range(1,n):
            obstacleGrid[0][j] = int(obstacleGrid[0][j-1] and (obstacleGrid[0][j]==0))

        for i in range(1,m):
            for j in range(1,n):
                if(obstacleGrid[i][j]):
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        return obstacleGrid[-1][-1]
        # m = len(obstacleGrid)
        # n = len(obstacleGrid[0])
        # dp = [[0]*n for _ in range(m)]

        # for i in range(m):
        #     if(obstacleGrid[i][0]!=1):
        #         dp[i][0] = dp[i-1][0] if i>0 else 1
        
        # for j in range(n):
        #     if(obstacleGrid[0][j]!=1):
        #         dp[0][j] = dp[0][j-1] if j>0 else 1

        # for i in range(1,m):
        #     for j in range(1,n):
        #         if(obstacleGrid[i][j]!=1):
        #             if(obstacleGrid[i-1][j]!=1):
        #                 dp[i][j] += dp[i-1][j]
        #             if(obstacleGrid[i][j-1]!=1):
        #                 dp[i][j] += dp[i][j-1]

        # return dp[-1][-1]
