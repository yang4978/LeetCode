class Solution:
    def totalNQueens(self, n: int) -> int:
        def dfs(x,col,queen,n,res):
            if x==n:
                res += 1
                return res
            
            for j in range(n):
                if not col[j]:
                    flag = 1
                    for xq,yq in queen:
                        if abs(x-xq)==abs(j-yq):
                            flag = 0
                            break
                    if flag:
                        queen.add((x,j))
                        col[j] = True
                        res = dfs(x+1,col,queen,n,res)
                        queen.remove((x,j))
                        col[j] = False
            return res

        col = [False]*n
        res = 0
        queen = set()
        res = dfs(0,col,queen,n,res)

        return res
