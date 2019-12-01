class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        num = [str(i) for i in range(1,n+1)]
        res = ''
        fac = 1
        for i in range(1,n):
            fac *= i

        if k==n*fac:
            return "".join(reversed(num))
        
        n -= 1

        while k:
            while fac>k:
                fac//=n
                n -= 1
                res += num.pop(0)
            
            if fac==k:
                res += num.pop(0) + "".join(reversed(num))
                return res
            else:
                res += num.pop((k-1)//fac)
                t = (k-1)//fac
                k -= t*fac
                fac //= n
                n -= 1
            
        return res
