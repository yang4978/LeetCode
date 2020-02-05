class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # nums = collections.defaultdict(list)

        # l = len(arr)
        
        # dp = [1]*l

        # for i in range(l):
        #     nums[arr[i]] = i
        #     temp = arr[i] - difference
        #     if temp in nums:
        #         dp[i] = 1+dp[nums[temp]]

        # return max(dp)

        dp = {}

        for i in arr:
            dp[i] = 1
            if i - difference in dp:
                dp[i] = dp[i-difference] + 1
            
        return max(dp.values())
