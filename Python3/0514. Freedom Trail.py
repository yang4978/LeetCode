class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        
        l = len(key)

        key = re.sub(r'([a-z])(\1*)',r'\1',key)

        m = len(key)
        n = len(ring)

        letter = collections.defaultdict(list)

        for i in range(n):
            letter[ring[i]].append(i)

        dp = [[float('inf')]*n for _ in range(m)]

        for i in range(n):
            if ring[i] == key[0]:
                dp[0][i] = min(i,n-i)
        
        for i in range(1,m):
            for j in range(n):
                if ring[j] == key[i]:
                    dp[i][j] = min(dp[i-1][index]+min(abs(j-index),n-abs(j-index)) for index in letter[key[i-1]])
        
        return min(dp[m-1]) + l
