class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l = len(nums)
        left,right = 0,0
        sum_value = 0
        res = l+1
        while right<l:
            sum_value += nums[right]
            while sum_value >= s:
                res = min(res,right-left+1)
                sum_value -= nums[left]
                left += 1
            right += 1

        return 0 if res == l+1 else res
