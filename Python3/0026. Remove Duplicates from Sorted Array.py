class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # l = len(nums)
        # i = 0
        # while(i<l-1):
        #     if(nums[i+1]==nums[i]):
        #         nums.pop(i)
        #         l -= 1
        #     else:
        #         i += 1
        # return l
        l = len(nums)
        p = 0
        q = 1
        while(q<l):
            if(nums[q]!=nums[p]):
                if(q-p>1):
                    nums[p+1] = nums[q]
                p += 1
            q += 1
        return p+1
