class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x1 = 0
        x2 = 0
        for i in nums:
            x2 ^= x1 & i
            x1 ^= i
            mask = ~(x1&x2)
            x2 &= mask
            x1 &= mask
        return x1
        # nums.sort()
        # l = len(nums)
        # for i in range(0,l-1,3):
        #     if(nums[i+1]!=nums[i]):
        #         return nums[i]
        # return nums[l-1]
