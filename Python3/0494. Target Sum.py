class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        num_sum  = sum(nums)
        if(S>num_sum or (num_sum-S)%2):
            return 0
        
        N = (num_sum-S)//2
        
        dp = [1]+[0]*N
        
        
        for j in nums:
            for i in range(N,j-1,-1):
                dp[i] = dp[i] + dp[i-j]

        return dp[-1]
        
#         num_sum = sum(nums)
#         if(S>num_sum):return 0
#         n = len(nums)
#         dp = [[0]*(2*num_sum+1) for i in range(n+1)]
        
#         dp[0][num_sum] = 1
        
#         for i in range(1,n+1):
#             for j in range(2*num_sum+1):
#                 if(j-nums[i-1]+num_sum>=0):
#                     dp[i][j] += dp[i-1][j-nums[i-1]]
                    
   
#                 if(j+nums[i-1]<2*num_sum+1):
#                     dp[i][j] += dp[i-1][j+nums[i-1]]          
#         return dp[-1][S+num_sum]
