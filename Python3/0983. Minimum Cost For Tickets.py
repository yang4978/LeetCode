class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # end = days[-1] + 1
        # dp = [0]*end
        # for d in range(1,end):
        #     temp = dp[d-1] + costs[0]
        #     temp = min(temp,min(dp[max(0,d-7):d])+costs[1])
        #     temp = min(temp,min(dp[max(0,d-30):d])+costs[2])
        #     if d not in days:
        #         temp = min(temp,dp[d-1])
        #     dp[d] = temp
        # return dp[-1]

        ans = [0]*(days[-1]+30)

        for d in range(len(ans)):
            if d in days:
                ans[d] = min(ans[d-1]+costs[0],ans[d-7]+costs[1],ans[d-30]+costs[2])
            else:
                ans[d] = ans[d-1]
        
        return ans[-1]
