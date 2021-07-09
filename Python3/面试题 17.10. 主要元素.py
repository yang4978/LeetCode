class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums.sort()
        # x = nums[len(nums)//2]
        # return x if nums.count(x) > len(nums) // 2 else -1

        count = 0
        major = 0
        for n in nums:
            if count == 0:
                major = n
            count += (1 if n == major else -1)

        count = 0
        
        for n in nums:
            if(n == major):
                count += 1
        
        return (major if count > len(nums) // 2 else -1)
