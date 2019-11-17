class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        l = len(costs)
        if(l==0): return 0
        if(l==1): return min(costs[0])
        
        k = len(costs[0])
        dp = [k*[0] for _ in range(l+1)]

        for i in range(1,l+1):
            min_1 = min(dp[i-1][:])
            j_1 = dp[i-1][:].index(min_1)

            min_2 = sorted(dp[i-1][:])[1]
            for j in range(k):
                dp[i][j] = costs[i-1][j] + (min_1 if j!=j_1 else min_2)
        
        return min(dp[-1][:])
