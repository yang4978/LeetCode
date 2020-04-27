class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        ret = functools.reduce(lambda x, y: x^y, nums)
        det = 1
        while det & ret == 0:
            det <<= 1
        a, b = 0, 0
        for n in nums:
            if n & det:
                a ^= n
            else:
                b ^= n
        
        return [a,b]
