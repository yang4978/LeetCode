#https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = {}
        for i in range(len(nums)):
            if(nums[i] in diff_dict):
                return [diff_dict[nums[i]],i]
            else:
                diff_dict[target-nums[i]] = i;
        # num_dict = {}
        # for i in range(len(nums)):
        #     if(nums[i] not in num_dict):
        #         num_dict[nums[i]] = [i]
        #     else:
        #         num_dict[nums[i]].append(i)
        #     if(target==2*nums[i] and len(num_dict[nums[i]])==2):
        #         return num_dict[nums[i]]
        #     elif(target!=2*nums[i] and target-nums[i] in num_dict):
        #         return [*num_dict[target-nums[i]],i]
