class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [grid[0][0]]
        for i in grid[0][1:]:
            dp.append(dp[-1]+i)

        for i in range(1,m):
            for j in range(n):
                dp[j] = grid[i][j] + (min(dp[j-1],dp[j]) if j>0 else dp[j])
        
        return dp[-1]
