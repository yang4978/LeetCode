class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [True]+[False]*(n)
        
        word = {}
        for i in wordDict:
            word[i] = len(i)
        
        for i in range(n+1):
            for w in wordDict:

                if(dp[i] and w==s[i:i+word[w]]):
                    dp[i+word[w]] = True
        return dp[-1]
