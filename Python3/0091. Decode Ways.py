class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=='0': return 0
        n = len(s)
        dp = [0]*(n+1)
        ppre = 1
        pre = 1

        for i in range(2,n+1):
            temp = 0
            if(s[i-1]!='0'):
                temp += pre
            if(s[i-2]!='0' and 10*int(s[i-2])+int(s[i-1])<=26):
                temp += ppre
            pre,ppre = temp,pre

        return pre
        # if s[0]=='0': return 0
        # n = len(s)
        # dp = [0]*(n+1)
        # dp[0] = 1
        # dp[1] = 1
        # for i in range(2,n+1):
        #     if(s[i-1]!='0'):
        #         dp[i] += dp[i-1]
        #     if(s[i-2]!='0' and 10*int(s[i-2])+int(s[i-1])<=26):
        #         dp[i] += dp[i-2]

        # return dp[-1]
