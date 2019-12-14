class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 1
        l = len(nums)
        if l<2:
            return l
        
        for fast in range(2,l):
            if nums[slow-1]!=nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
        
        return slow+1

        # i,j = 0,0
        # l = len(nums)
        # dis = 0
        # total = 0

        # while i<l and j<l:
        #     while j<l and nums[j]==nums[i]:
        #         j += 1

        #     dis = j-i-total
        #     total += max(0,dis-2)

        #     if total:
        #         i = i + min(dis,2)
        #         k = i
        #         while k<j:
        #             if j>=l:
        #                 break
        #             nums[k] = nums[j]
        #             k += 1
        #     else:
        #         i = j
            
        # return l-total
