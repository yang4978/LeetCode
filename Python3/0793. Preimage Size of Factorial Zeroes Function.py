class Solution:
    def preimageSizeFZF(self, K: int) -> int:
        def zeta(x):
            if x == 0:
                return 0
            return x//5 + zeta(x//5)
        
        lo = 0
        hi = 10*K+1

        while lo<hi:
            mid = (lo+hi)//2
            x = zeta(mid)
            if x == K:
                return 5
            
            elif x<K:
                lo = mid + 1
            
            else:
                hi = mid
        
        return 0
