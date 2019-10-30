class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        num_sum = sum(nums)
        if(num_sum%2): return False
        target = num_sum//2
        n = len(nums)
        dp = [[False]*(target+1) for i in range (n)]
        
        for i in range(target+1):
            dp[0][i] = nums[0]==i
        
        for i in range(1,n):
            for j in range(target+1):
                if(j>=nums[i]):
                    dp[i][j] = (dp[i-1][j]|dp[i-1][j-nums[i]])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]
        
        
#         l = len(nums)
#         num_sum = sum(nums)
#         if(num_sum%2): return False
#         n = num_sum//2
#         memo = [False]*(n+1)
        
#         for i in range(n+1):
#             memo[i] = (nums[0]==i)

#         for i in range(1,l):
#             for j in range(n,nums[i]-1,-1):
#                 memo[j] = (memo[j]|memo[j-nums[i]])
        
#         return memo[n]
