class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        x = nums[len(nums)//2]
        return x if nums.count(x) > len(nums) // 2 else -1
