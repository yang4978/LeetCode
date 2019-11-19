class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -float('inf')
        imax = 1
        imin = 1

        for i in range(len(nums)):
            if(nums[i]<0):
                imin,imax = imax,imin
            
            imax = max(imax*nums[i],nums[i])
            imin = min(imin*nums[i],nums[i])
            
            res = max(res,imax)
        
        return res
