class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        if(len(s3)!=m+n):
            return False
        dp = [[False]*(1+n) for _ in range(1+m)]

        dp[0][0] = True

        for i in range(1,1+m):
            dp[i][0] = dp[i-1][0] and s1[i-1]==s3[i-1]
        
        for j in range(1,1+n):
            dp[0][j] = dp[0][j-1] and s2[j-1]==s3[j-1]
        
        for i in range(1,1+m):
            for j in range(1,1+n):
                dp[i][j] = (s1[i-1]==s3[i+j-1] and dp[i-1][j]) or (s2[j-1]==s3[i+j-1] and dp[i][j-1])
        
        return dp[-1][-1]
