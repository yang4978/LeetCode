class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i,j = 0,0

        while j<len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j-1]:
                j += 1
            else:
                return False
        
        return i == len(name)

        # i,j = 0,0
        # x = len(name)
        # y = len(typed)
        # while(i<x and j<y):
        #     if(name[i]==typed[j]):
        #         i += 1
        #         j += 1
        #     elif(typed[j]==name[max(0,i-1)]):
        #         j += 1
        #     else:
        #         return False

        # if i == x:
        #     while j<y:
        #         if typed[j] == name[i-1]:
        #             j += 1
        #         else:
        #             return False

        # if(j==y and i<x):
        #     return False
        # else:
        #     return True


        # y = len(typed)
        # x = len(name)
        
        # dp = [[False]*(y+1) for _ in range(x+1)]
        # dp[0][0] = True
        # for j in range(1,y+1):
        #     if(typed[j-1]==name[0]):
        #         dp[0][j] = dp[0][j-1]

        # for i in range(1,x+1):
        #     for j in range(1,y+1):
        #         if(name[i-1]==typed[j-1]):
        #             dp[i][j] = True and (dp[i-1][j-1] or dp[i][j-1])
        #         elif(typed[j-1]==typed[j-2]):
        #             dp[i][j] = dp[i][j-1] and True

        # return dp[-1][-1]
