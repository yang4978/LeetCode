class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # i,j = 0,0
        # for i in range(len(nums)):
        #     if nums[i]!=val:
        #         nums[j] = nums[i]
        #         j += 1
        # return j
        n = len(nums)
        i = 0
        while(i<n):
            if nums[i]==val:
                nums[i] = nums[n-1]
                n -= 1
            else:
                i += 1
        
        return n
