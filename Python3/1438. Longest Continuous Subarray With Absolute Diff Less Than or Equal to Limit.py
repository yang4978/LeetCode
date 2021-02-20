class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_num = float('inf')
        max_num = -float('inf')
        l = 0
        r = 0

        while r < len(nums):
            if nums[r] > max_num:
                max_num = nums[r]
            if nums[r] < min_num:
                min_num = nums[r]
            
            r += 1

            if max_num - min_num > limit:
                if nums[l] == max_num:
                    max_num = max(nums[l+1:r])
                if nums[l] == min_num:
                    min_num = min(nums[l+1:r])

                l += 1
        
        return r-l
                
