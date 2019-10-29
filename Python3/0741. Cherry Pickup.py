class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[[-1]*(n+1) for i in range(n+1)] for j in range(n+1)]
        dp[1][1][1] = grid[0][0]
        
        for i in range(1,n+1):
            for j in range(1,n+1):
                for k in range(1,n+1):
                    l = i+j-k
                    if(l<1 or l>n):
                        continue
                    if(grid[i-1][j-1]!=-1 and grid[k-1][l-1]!=-1):
                        temp = max(dp[i-1][j][k],dp[i][j-1][k],dp[i-1][j][k-1],dp[i][j-1][k-1])
                        if(temp<0): continue
                        dp[i][j][k] = temp + grid[i-1][j-1] + (i!=k)*grid[k-1][l-1]
        return dp[n][n][n] if dp[n][n][n]>0 else 0
