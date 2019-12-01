class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        num = [str(i) for i in range(1,n+1)]
        res = ''
        step = math.factorial(n)

        while n:
            step //= n
            n -= 1
            idx = math.ceil(k/step)-1
            res += num.pop(idx)
            k -= idx*step
        
        return res

        # num = [str(i) for i in range(1,n+1)]
        # res = ''
        # fac = math.factorial(n-1)
        # n -= 1

        # while k:
        #     if fac>k:
        #         fac//=n
        #         n -= 1
        #         res += num.pop(0)
            
        #     if fac==k:
        #         res += num.pop(0) + "".join(reversed(num))
        #         return res

        #     else:
        #         idx = math.ceil(k/fac)-1
        #         res += num.pop(idx)
        #         k -= idx*fac
        #         fac //= n
        #         n -= 1
            
        # return res
