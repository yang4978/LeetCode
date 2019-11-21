class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        for i in num_set:
            temp = i
            cur = 1
            if (temp-1 not in num_set):
                while temp+1 in num_set:
                    cur += 1
                    temp += 1
            res = max(res,cur)
        return res

        # if nums == []:
        #     return 0
        # nums.sort()
        # n = len(nums)
        # dp = [1]*n
        # for i in range(1,n):
        #     if nums[i]==nums[i-1]+1:
        #         dp[i] = dp[i-1]+1
        #     elif nums[i] == nums[i-1]:
        #         dp[i] = dp[i-1]
        
        # return max(dp)
