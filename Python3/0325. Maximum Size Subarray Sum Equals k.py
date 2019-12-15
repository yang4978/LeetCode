class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        l = len(nums)
        nums = [0]+nums
        sum_dict = {k:0}
        res = 0
        for i in range(1,l+1):
            nums[i] += nums[i-1]
            if nums[i] in sum_dict:
                res = max(res,i-sum_dict[nums[i]])
            if k+nums[i] not in sum_dict:
                sum_dict[k+nums[i]] = i
        return res
