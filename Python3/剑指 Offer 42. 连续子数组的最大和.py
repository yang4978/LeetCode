class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -100
        temp = 0

        for n in nums:
            temp = max(n, temp + n)
            res = max(res, temp)
        
        return res
