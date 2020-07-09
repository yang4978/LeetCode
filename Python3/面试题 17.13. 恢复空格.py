class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        d = {}
        for i in dictionary:
            d[i] = len(i)

        l = len(sentence)
        dp = [0]*(l+1)
        
        for i in range(l-1,-1,-1):
            dp[i] = dp[i+1] + 1

            for j in d:
                if sentence[i:i+d[j]] == j:
                    dp[i] = min(dp[i],dp[i+d[j]])

        return dp[0]
