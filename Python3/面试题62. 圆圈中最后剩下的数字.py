class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        f = 0
        for i in range(2,n+1):
            f = (f+m)%i
        
        return f
    # sys.setrecursionlimit(100000)

    # def f(self,n,m):
    #     if n == 1:
    #         return 0
    #     else:
    #         return (self.f(n-1,m) + m)%n

    # def lastRemaining(self, n: int, m: int) -> int:
    #     return self.f(n,m)
