class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        arr = sorted(nums)
        l = len(nums)
        start = l-1
        end = 0
        for i in range(l):
            if arr[i]!=nums[i]:
                start = i
                break
        
        for j in range(l-1,-1,-1):
            if arr[j]!=nums[j]:
                end = j
                break

        return end-start+1 if end>start else 0


        # l = len(nums)
        # min_val = float('inf')
        # max_val = -float('inf')

        # for i in range(1,l):
        #     if(nums[i]<nums[i-1]):
        #         min_val = min(min_val,nums[i])
        
        # for i in range(l-2,-1,-1):
        #     if(nums[i]>nums[i+1]):
        #         max_val = max(max_val,nums[i])
        
        # start,end = 0,0
        # for start in range(l):
        #     if nums[start]>min_val:
        #         break
        
        # for end in range(l-1,0,-1):
        #     if nums[end]<max_val:
        #         break

        # return 0 if start>=end else end-start+1
