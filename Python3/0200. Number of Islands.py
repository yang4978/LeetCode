class Solution:
    def dfs(self,grid,x,y,m,n):
        for dx,dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            if 0<=x+dx<m and 0<=y+dy<n and grid[x+dx][y+dy] == '1':
                grid[x+dx][y+dy] = '0'
                self.dfs(grid,x+dx,y+dy,m,n)

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)

        if m == 0:
            return 0

        n = len(grid[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid,i,j,m,n)

        return count

    # def numIslands(self, grid: List[List[str]]) -> int:

    #     m = len(grid)

    #     if m == 0:
    #         return 0

    #     n = len(grid[0])
    #     count = 0

    #     directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    #     for i in range(m):
    #         for j in range(n):
    #             if grid[i][j] == '1':
    #                 grid[i][j] = '0'
    #                 queue = []
    #                 queue.append((i,j))
    #                 count += 1

    #                 while queue:
    #                     x,y = queue.pop(0)
    #                     for dx,dy in directions:
    #                         if 0<=x+dx<m and 0<=y+dy<n and grid[x+dx][y+dy] == '1':
    #                             grid[x+dx][y+dy] = '0'
    #                             queue.append((x+dx,y+dy))
        
    #     return count
