class Solution:
    def mySqrt(self, x: int) -> int:
        pre = 0
        cur = x

        while abs(pre-cur)>=1:
            pre = cur
            cur = 0.5*(cur+x/cur)
        
        return int(cur)
