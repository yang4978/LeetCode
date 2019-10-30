class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1]+[0]*(target)
        
        for i in range(target+1):
            for j in nums:
                if(i>=j):
                    dp[i] += dp[i-j]
        return dp[-1]
