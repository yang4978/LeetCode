class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        l1 = len(s)
        l2 = len(p)
        dp = [[False]*(l2+1) for i in range(l1+1)]
        dp[0][0] = True
        
        for i in range(1,l2):
            dp[0][i+1] = (p[i]=='*') and dp[0][i-1]
        
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if(p[j-1]=='.' or p[j-1]==s[i-1]):
                    dp[i][j] = dp[i-1][j-1]
                
                elif(p[j-1]=='*'):
                    if(p[j-2]!=s[i-1] and p[j-2]!='.'):
                        dp[i][j] = dp[i][j-2]
                    else:
                        dp[i][j] = dp[i-1][j] or dp[i][j-1] or dp[i][j-2]
                        
        return dp[-1][-1]
