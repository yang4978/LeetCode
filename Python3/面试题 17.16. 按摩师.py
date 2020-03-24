class Solution:
    def massage(self, nums: List[int]) -> int:
        # l = len(nums)
        # res = [0]*(l+2)
        # for i in range(2,l+2):
        #     res[i] = max(res[i-2],res[i-3])+nums[i-2]
        
        # return max(res[-1],res[-2])

        pp, p = 0, 0
        for i in range(len(nums)):
            res = max(pp+ nums[i], p) 
            pp, p = p, res
        
        return p
