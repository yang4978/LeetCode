class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if(amount==0): return 0
        dp =[0]+[amount+1]*(amount)
        
        for i in range(1,amount+1):
            for j in coins:
                if(i>=j):
                    dp[i] = min(dp[i],dp[i-j]+1)
        
        return dp[-1] if dp[-1]<=amount else -1
        
        
