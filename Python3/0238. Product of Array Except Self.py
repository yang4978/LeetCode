class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)        
        res = [1]*n
        k = 1
        for i in range(n):
            res[i] = k
            k *= nums[i]
        
        k = 1
        for i in range(n-1,-1,-1):
            res[i] *= k
            k *= nums[i]
        
        return res
