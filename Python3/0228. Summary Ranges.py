class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # l = len(nums)
        # if l == 1:
        #     return [str(nums[0])]

        # left = 0
        # right = 1
        # res = []

        # while right <= l:
        #     if right == l or nums[right] != nums[right-1] + 1:
        #         if right == left + 1:
        #             res.append(str(nums[left]))
        #         else:
        #             res.append(str(nums[left])+'->'+str(nums[right-1]))
                
        #         left = right

        #     right += 1
        
        # return res

        l = len(nums)
        if l == 1:
            return [str(nums[0])]
            
        left = 0
        right = 0
        res = []

        while right < l:
            if right == l-1 or nums[right+1] != nums[right] + 1:
                if right == left:
                    res.append(str(nums[left]))
                else:
                    res.append(str(nums[left])+'->'+str(nums[right]))
                
                left = right + 1

            right += 1
        
        return res
        
