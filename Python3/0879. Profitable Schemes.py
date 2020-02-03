class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        l = len(group)

        mod = 10**9+7

        dp = [[0]*(G+1) for _ in range(P+1)]

        dp[0][0] = 1

        for i in range(l):
            dp2 = [row[:] for row in dp]

            for p in range(P+1):
                for g in range(G-group[i]+1):
                    dp2[min(p+profit[i],P)][g+group[i]] += dp[p][g]                

            dp = dp2

        return sum(dp[-1])%mod
