class Solution:
    def divisorGame(self, N: int) -> bool:

        return not N&1
        
        #return N%2==0

        # dp = [False]*(N+1)
        
        # for i in range(2,N+1):
        #     for j in range(1,i):
        #         if i%j==0 and dp[i-j]==False:
        #             dp[i] = True
        #             break
        
        # return dp[-1]
