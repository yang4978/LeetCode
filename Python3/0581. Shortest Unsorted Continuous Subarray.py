class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l = len(nums)
        min_val = float('inf')
        max_val = -float('inf')

        for i in range(1,l):
            if(nums[i]<nums[i-1]):
                min_val = min(min_val,nums[i])
        
        for i in range(l-2,-1,-1):
            if(nums[i]>nums[i+1]):
                max_val = max(max_val,nums[i])
        
        start,end = 0,0
        for start in range(l):
            if nums[start]>min_val:
                break
        
        for end in range(l-1,0,-1):
            if nums[end]<max_val:
                break

        return 0 if start>=end else end-start+1
