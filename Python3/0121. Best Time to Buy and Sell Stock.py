class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        temp = 0
        res = 0
        for i in range(len(prices)-1):
            temp = max(prices[i+1]-prices[i],temp+prices[i+1]-prices[i])

            res = max(temp,res)
        return res
