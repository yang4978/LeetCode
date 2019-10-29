class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if(n==1):
            return nums[0]
        
        left = 0
        right = n-1
        
        if(nums[right]>nums[0]):
            return nums[0]
        
        while(right>=left):
            mid = left + (right-left)//2
            if(nums[mid]>nums[mid+1]):
                return nums[mid+1]
            
            if(nums[mid]<nums[mid-1]):
                return nums[mid]
            
            if(nums[mid]>nums[0]):
                left = mid + 1
            else:
                right =mid - 1
        
        # n = len(nums)
        # for i in range(1,n):
        #     if(nums[i-1]>nums[i]):
        #         return nums[i]
        # return nums[0]
