class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        memo = {}
        
        def dp(k,n):
            if (k,n) not in memo:
                if n == 0:
                    ans = 0
                
                elif k == 1:
                    ans = n
                
                else:
                    lo = 1
                    hi = n

                    while lo < hi:
                        x = (lo + hi)//2
                        t1 = dp(k-1, x-1)
                        t2 = dp(k, n-x)

                        if t1 < t2:
                            lo = x + 1
                        elif t1 > t2:
                            hi = x
                        else:
                            lo = hi = x
                    
                    ans = 1 + min(max(dp(k-1,i-1),dp(k,n-i)) for i in (lo,hi))
                
                memo[k,n] = ans
            
            return memo[k,n]

        return dp(K,N)
