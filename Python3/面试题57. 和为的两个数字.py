class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # digit = set()
        
        # for i in nums:
        #     if i in digit:
        #         return [i,target-i]
        #     else:
        #         digit.add(target-i)
        
        i = 0
        j = len(nums) - 1

        while i<j:
            temp = nums[i] + nums[j]
            if temp == target:
                return [nums[i],nums[j]]
            elif temp > target:
                j -= 1
            else:
                i += 1
