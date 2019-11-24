class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        flag = 1

        if dividend<0:
            flag = -flag
            dividend = -dividend
        
        if divisor<0:
            flag = -flag
            divisor = -divisor
        
        res = 0
        while(dividend>=divisor):
            t = divisor
            n = 1
            while(dividend>=t):
                dividend -= t
                res += n
                t <<= 1
                n <<= 1
        
        res = -res if flag==-1 else res

        return res if -(1<<31)<=res<=(1<<31)-1 else (1<<31)-1
        #return min(max(-(1<<31),res),(1<<31)-1)
