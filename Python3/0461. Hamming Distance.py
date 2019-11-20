class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # n = x^y
        # res = 0
        # while n:
        #     res += n%2
        #     n //= 2
        # return res
        res = 0
        mask = 1
        while(mask<=x or mask<=y):
            res += mask&x!=mask&y
            mask <<= 1
        return res
