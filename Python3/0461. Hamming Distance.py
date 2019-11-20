class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        n = len(nums)

        mask = 1
        for i in range(32):
            temp = 0
            for j in nums:
                temp += mask&j!=0
            res += temp*(n-temp)
            mask <<= 1
        
        return res
