# class Solution:
#     def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
#         nums.sort()
#         dp = [[i] for i in nums]
#         res = []
#         for i in range(len(nums)):
#             for j in range(i):
#                 if nums[i]%nums[j]==0 and len(dp[j])+1>len(dp[i]):
#                     dp[i] = dp[j]+nums[i:i+1]
#             if len(dp[i])>len(res):
#                 res = dp[i]
#         return res

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        l = len(nums)
        dp = [1] * l

        for i in range(1, l):
            for j in range(i - 1, - 1 ,-1):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        target = max(dp)
        i = l - 1
        res = [0] * target
        while target:
            if(dp[i] == target and (target == len(res) or res[target] % nums[i] == 0)):
                res[target - 1] = nums[i]
                target -= 1
            i -= 1
        
        return res

