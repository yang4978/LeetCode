class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        island = 0

        def dfs(grid,m,n,x,y,directions):
            for dx,dy in directions:
                if 0<=x+dx<m and 0<=y+dy<n and grid[x+dx][y+dy]==0:
                    grid[x+dx][y+dy] = 1
                    dfs(grid, m, n, x+dx, y+dy,directions)

            if x==0 or x==m-1 or y==0 or y==n-1:
                nonlocal flag
                flag = 0
        

        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    grid[i][j] = 1
                    flag = 1
                    dfs(grid, m, n, i, j,directions)
                    island += flag

        return island

        # if not grid:
        #     return 0

        # m = len(grid)
        # n = len(grid[0])
        # directions = [(-1,0),(1,0),(0,-1),(0,1)]

        # res = 0

        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j]==0:
        #             stack = [(i,j)]
        #             closed = 1
        #             while stack:
        #                 x,y = stack.pop(0)
        #                 if x==0 or x==m-1 or y==0 or y==n-1:
        #                     closed = 0
        #                 grid[x][y] = 1
        #                 for dx,dy in directions:
        #                     if 0<=x+dx<m and 0<=y+dy<n and grid[x+dx][y+dy] == 0:
        #                         stack.append((x+dx,y+dy))
        #                         grid[x+dx][y+dy] = 1
        #             res += closed

        # return res
