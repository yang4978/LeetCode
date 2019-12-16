class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum_dict = {0:-1}
        temp = 0
        res = 0
        for i in range(len(nums)):
            temp += 1 if nums[i] else -1

            if temp not in sum_dict:
                sum_dict[temp] = i
            else:
                res = max(res,i - sum_dict[temp])
        return res
