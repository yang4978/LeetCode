class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        # s = set()
        # for i in nums:
        #     if i in s:
        #         return i
        #     s |= {i}
        for i in range(len(nums)):
            if nums[i] != i:
                x = nums[i]
                if nums[x] == x:
                    return x
                nums[x],nums[i] = nums[i],nums[x]
                
