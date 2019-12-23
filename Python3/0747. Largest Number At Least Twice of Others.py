class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_value = max(nums)
        for i in nums:
            if i==max_value:
                continue
            if i*2>max_value:
                return -1
        
        return nums.index(max_value)
