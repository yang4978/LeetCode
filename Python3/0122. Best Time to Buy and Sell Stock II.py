class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(prices==[]):
            return 0
        l = len(prices)
        res = 0
        for i in range(1,l):
            if(prices[i]>prices[i-1]):
                res += prices[i]-prices[i-1]
        return res
