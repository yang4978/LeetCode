class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x, y, temp_index, marked):
            if temp_index == l:
                return True
            res = False
            for dx, dy in directions:
                if 0<=x+dx<m and 0<=y+dy<n and marked[x+dx][y+dy] == 0 and board[x+dx][y+dy] == word[temp_index]:
                    
                    marked[x+dx][y+dy] = 1
                    res = res or dfs(x+dx,y+dy,temp_index+1,marked)
                    marked[x+dx][y+dy] = 0
            return res

        m = len(board)
        n = len(board[0])
        l = len(word)

        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        res = False
        used = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    index = 1
                    used[i][j] = 1
                    res = res or dfs(i,j,index,used)
                    used[i][j] = 0

        return res

#         def dfs(board,m,n,i,j,word,used):
#             if len(word)==0:
#                 return True
            
#             for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
#                     if 0<=i+di<m and 0<=j+dj<n and board[i+di][j+dj]==word[0] and not used[i+di][j+dj]:
#                         used[i+di][j+dj] = True
#                         if dfs(board,m,n,i+di,j+dj,word[1:],used)==True:
#                             return True
#                         else:
#                             used[i+di][j+dj] = False
#             return False

#         m = len(board)
#         n = len(board[0])
#         used = [[False]*n for _ in range(m)]
#         res = False

#         for i in range(m):
#             for j in range(n):
#                 if(board[i][j]==word[0]):
#                     used[i][j] = True
#                     if dfs(board,m,n,i,j,word[1:],used) == True:
#                         return True
#                     else:
#                         used[i][j] = False

#         return False

