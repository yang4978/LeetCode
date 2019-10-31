class Solution:
    n = len(M)
    state = [False]*n
    count = 0

    def dfs(i):
        state[i] = True
        for j in range(n):
            if(M[i][j] and state[j]==False):
                dfs(j)

    for i in range(n):
        if(state[i]==False):
            dfs(i)
            count += 1
    return count

#     def dfs(self,M,state,i):
#         for j in range(len(M)):
#             if(M[i][j] and state[j]==0):
#                 state[j] = 1
#                 self.dfs(M,state,j)
    
#     def findCircleNum(self, M: List[List[int]]) -> int:
#         n = len(M)
#         state = [0]*n
#         count = 0
#         for i in range(n):
#             if(state[i]==0):
#                 self.dfs(M,state,i)
#                 count += 1
#         return count
        
