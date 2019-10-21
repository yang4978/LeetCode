#https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = {}
        for i in range(len(nums)):
            if(nums[i] in diff_dict):
                return [diff_dict[nums[i]],i]
            else:
                diff_dict[target-nums[i]] = i;
