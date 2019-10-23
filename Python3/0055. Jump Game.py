class Solution:
    def canJump(self, nums: List[int]) -> bool:
        k = 0
        for i in range(len(nums)):
            if(i>k):return False
            if(k>len(nums)):return True
            k = max(k,i+nums[i])
        return True
        # i = 0
        # index = 0
        # temp = 0
        # while(i<len(nums)):
        #     if(i+nums[i]>=len(nums)-1):
        #         return True
        #     for j in range(nums[i],0,-1):
        #         if(i+j+nums[i+j]>=temp):
        #             index = i+j
        #             temp = i+j+nums[i+j]
        #     i = index
        #     if(nums[i]==0): return False
        # return True
