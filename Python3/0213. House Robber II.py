class Solution:
    def rob(self, nums: List[int]) -> int:
        def room(nums):
            cur,pre = 0,0
            for num in nums:
                pre,cur = cur, max(pre+num,cur)
            return cur
        
        return max(room(nums[1:]),room(nums[:-1])) if len(nums)!=1 else nums[0]
