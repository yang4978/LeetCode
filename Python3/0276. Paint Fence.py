class Solution:
    def numWays(self, n: int, k: int) -> int:
        if(n==0 or k==0): return 0
        if(n==1): return k
        dp = [1]*(1+n)
        dp[1] = k
        dp[2] = k*k
        for i in range(3,1+n):
            dp[i] = dp[i-1]*(k-1) + dp[i-2]*(k-1)
        return dp[-1]
