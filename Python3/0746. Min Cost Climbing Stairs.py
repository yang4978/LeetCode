class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # n = len(cost)
        # dp = [0]*(n+2)

        # for i in range(n):
        #     dp[i+2] = cost[i] + min(dp[i],dp[i+1])
        
        # return min(dp[-1],dp[-2])

        pre, cur = 0,0

        for c in reversed(cost):
            pre, cur = c+min(pre,cur), pre
        
        return min(cur,pre)
