class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        i = l-2
        while(i>=0):
            if nums[i+1]>nums[i]:
                break
            i -= 1

        if i==-1:
            nums.reverse()
            return

        j = l-1
        while(j>i):
            if nums[j]>nums[i]:
                break
            j -= 1
        
        nums[i],nums[j] = nums[j],nums[i]
        nums[i+1:] = reversed(nums[i+1:])
        
