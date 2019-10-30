class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0]*(n+1) for i in range(m+1)]
        
        for item in strs:
            item_0 = item.count('0')
            item_1 = item.count('1')
            
            for i in range(m,item_0-1,-1):
                for j in range(n,item_1-1,-1):
                    dp[i][j] = max(dp[i][j],1+dp[i-item_0][j-item_1])
                            
        return dp[-1][-1]
                
