class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if K==1:
            return 0
        t = 1<<N
        while(t>=K and N>0):
            t >>= 1
            N -= 1
        return 1 - self.kthGrammar(N,K-(1<<N))

        # if K == 1:
        #     return 0
        
        # if K <= 1<<N-2:
        #     return self.kthGrammar(N-1,K)
        
        # return 1-self.kthGrammar(N-1,K-(1<<N-2))
