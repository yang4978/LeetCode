class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        temp = 0

        for i in nums+[0]:
            if i:
                temp += 1
            else:
                res = max(res,temp)
                temp = 0
        
        return res
