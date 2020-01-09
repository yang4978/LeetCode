class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if not m:
            return 0
        
        n = len(grid[0])

        directions = [(0,-1),(0,1),(-1,0),(1,0)]

        res = 0
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue = [(i,j)]
                    grid[i][j] = 0
                    count = 1
                    while queue:
                        x,y = queue.pop(0)
                        for dx,dy in directions:
                            if 0<=x+dx<m and 0<=y+dy<n and grid[x+dx][y+dy] == 1:
                                queue.append((x+dx,y+dy))
                                count += 1
                                grid[x+dx][y+dy] = 0
                res = max(res,count)
        
        return res
