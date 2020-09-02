class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        return sorted(nums,key = lambda x:(x+1)&1)
        # i = 0
        # j = len(nums) - 1

        # while i<j:
        #     while i<j and nums[i]&1 == 1 : i += 1
        #     while i<j and nums[j]&1 == 0 : j -= 1
        #     nums[i], nums[j] = nums[j], nums[i]
        
        # return nums
