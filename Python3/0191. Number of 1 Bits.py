class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        mask = 1
        for i in range(32):
            res += (n&mask!=0)
            mask <<= 1
        return res
        # res = 0
        # while n:
        #     res += n%2
        #     n //= 2
        # return res
