class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def overlap(s, ss):
            return len(set(s) & set(ss)) > 0

        l = len(arr)
        dp = [[[] for x in range(26 + 1)] for _ in range(l + 1)]

        for x in arr:
            temp = []
            for y in arr:
                if not overlap(x,y):
                    temp.append([y, len(y)])

        for i in range(1, l + 1):
            flag = True
            s = arr[i - 1]

            if(len(s) == len(set(s))):
                flag = False
                dp[i][len(s)].append(s)

            for j in range(26, -1 ,-1):
                if dp[i - 1][j] != []:
                    dp[i][j] += dp[i - 1][j]
                    if flag: 
                        continue
                    for ss in dp[i - 1][j]:
                        if not overlap(s, ss):
                            dp[i][j + len(s)].append(s + ss)

        for j in range(26, -1, -1):
            if dp[-1][j] != []:
                return j
        
        return 0
