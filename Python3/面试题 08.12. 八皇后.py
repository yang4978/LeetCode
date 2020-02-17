class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def arrange(t,index,i,n):
            for row in range(index,n):
                t[row][i] = 1
            directions = [(1,-1),(1,1)]

            for dx,dy in directions:
                x = index
                y = i
                while x+dx<n and 0<=y+dy<n:
                    t[x+dx][y+dy] = 1
                    x += dx
                    y += dy
            return t


        def dfs(n,index,used,arr):
            if index == n:
                res.append(['.'*i + 'Q' + '.'*(n-1-i) for i in arr])
                return

            for i in range(n):
                if used[index][i] == 0:
                    temp = arrange([row[:] for row in used],index,i,n)
                    dfs(n,index+1,temp,arr+[i])
            
            return

        res = []
        dfs(n,0,[[0]*n for _ in range(n)],[])
        return res
