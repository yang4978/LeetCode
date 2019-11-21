class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        hold = -float('inf')
        rest = 0
        sold = 0

        for i in range(n):
            tmp_hold = hold
            hold = max(hold,rest-prices[i])
            rest = max(rest,sold)
            sold = tmp_hold + prices[i]
        
        return max(rest,sold)
        
        # return max(hold[-1],rest[-1],sold[-1])
        # n = len(prices)
        # hold = [-float('inf')]*(n+1)
        # rest = [0]*(n+1)
        # sold = [0]*(n+1)

        # for i in range(1,n+1):
        #     hold[i] = max(hold[i-1],rest[i-1]-prices[i-1])
        #     rest[i] = max(rest[i-1],sold[i-1])
        #     sold[i] = hold[i-1]+prices[i-1]
        
        # return max(hold[-1],rest[-1],sold[-1])
