class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        l = len(costs)
        dp = [[0]*3 for _ in range(l+1)]

        for i in range(1,l+1):
            for j in range(3):
                temp = float('inf')
                for k in range(3):
                    if k!=j:
                        temp = min(temp,dp[i-1][k])
                dp[i][j] = costs[i-1][j] + temp
        
        return min(dp[-1][:])
