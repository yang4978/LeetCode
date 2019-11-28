class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
                
        def dfs(x,col,queen,n,res):
            if x==n:
                res.append(['.'*j+'Q'+(n-j-1)*'.' for i,j in queen])
                # t = [0]*n
                # for i,j in queen:
                #     t[i] = '.'*j+'Q'+(n-j-1)*'.'
                # res.append(t)
                return
            
            for j in range(n):
                if not col[j]:
                    flag = 1
                    for xq,yq in queen:
                        if abs(x-xq)==abs(j-yq):
                            flag = 0
                            break
                    if flag:
                        queen.append((x,j))
                        #queen.add((x,j))
                        col[j] = True
                        dfs(x+1,col,queen,n,res)
                        queen.pop()
                        #queen.remove((x,j))
                        col[j] = False

        col = [False]*n
        res = []
        #queen = set()
        queen = []
        dfs(0,col,queen,n,res)

        return res
    
        # col = [False]*n

        # def dfs(x,col,queen,n,res):
        #     if x==n:
        #         res.append(queen.copy())
        #         return
            
        #     for j in range(n):
        #         if not col[j]:
        #             flag = 1
        #             for xq,yq in queen:
        #                 if abs(x-xq)==abs(j-yq):
        #                     flag = 0
        #                     break
        #             if flag:
        #                 queen.add((x,j))
        #                 col[j] = True
        #                 dfs(x+1,col,queen,n,res)
        #                 queen.remove((x,j))
        #                 col[j] = False

        # res = []
        # queen = set()
        # dfs(0,col,queen,n,res)

        # ans = []
        
        # for pairs in res:
        #     board = [['.']*n for _ in range(n)]
        #     for i,j in pairs:
        #         board[i][j] = 'Q'
        #     ans.append(["".join(i) for i in board])

        # return ans
