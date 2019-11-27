class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            return 1/self.myPow(x,-n)
        
        if n==0:
            return 1
        
        if n==1:
            return x
        
        half = self.myPow(x,n//2)
        res = self.myPow(x,n%2)

        return half*half*res

        # if n < 0:
        #     return 1/self.myPow(x,-n)
        
        # if n == 0:
        #     return 1
        
        # res = 1
        # while(n):
        #     power = 1
        #     t = x
        #     while(power<=n):
        #         n -= power
        #         res *= t
        #         t *= t
        #         power <<= 1
        
        # return res
