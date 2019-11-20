class Solution(object):
    def lengthOfLIS(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
        n = len(nums)
        res = 0
        state = [0]*n
        for num in nums:
            i,j = 0,res
            while(i<j):
                m = (i+j)//2
                if state[m]<num:
                    i = m+1
                else:
                    j = m
            state[i] = num
            if j==res:
                res += 1
        
        return res

        # n = len(nums)
        # if n==0:
        #     return 0

        # dp = [0 for _ in range(n+1)]
        
        # dp[1] = 1

        # for i in range(1,n+1):
        #     k = i-1
        #     temp = 0
        #     while(k):
        #         if(nums[i-1]>nums[k-1]):
        #             temp = max(temp,dp[k])
        #         k -= 1
        #     dp[i] = temp + 1
        
        # return max(dp)
