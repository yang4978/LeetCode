class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(board,m,n,i,j,word,used):
            if len(word)==0:
                return True
            
            for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                    if 0<=i+di<m and 0<=j+dj<n and board[i+di][j+dj]==word[0] and not used[i+di][j+dj]:
                        used[i+di][j+dj] = True
                        if dfs(board,m,n,i+di,j+dj,word[1:],used)==True:
                            return True
                        else:
                            used[i+di][j+dj] = False
            return False

        m = len(board)
        n = len(board[0])
        used = [[False]*n for _ in range(m)]
        res = False

        for i in range(m):
            for j in range(n):
                if(board[i][j]==word[0]):
                    used[i][j] = True
                    if dfs(board,m,n,i,j,word[1:],used) == True:
                        return True
                    else:
                        used[i][j] = False

        return False

