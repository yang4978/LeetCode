class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        dis = collections.defaultdict(list)
        for i in flights:
            dis[i[0]].append(i[1:])

        dp = [[-1]*n for _ in range(K+1)]

        for i in dis[src]:
            dp[0][i[0]] = i[1]
        
        for i in range(1,K+1):
            for j in range(n):
                if dp[i-1][j] != -1:
                    if(dp[i][j]==-1 or dp[i-1][j]<dp[i][j]):
                        dp[i][j] = dp[i-1][j]
                    for k1,k2 in dis[j]:
                        if(dp[i][k1]==-1 or dp[i][k1]>dp[i-1][j]+k2):
                            dp[i][k1] = dp[i-1][j]+k2
        
        print(*dp,sep='\n')
        
        return dp[K][dst]
