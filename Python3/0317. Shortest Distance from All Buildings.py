class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if not m:
            return -1
        n = len(grid[0])

        building = 0
        dist = [[0]*n for _ in range(m)]
        count = [[0]*n for _ in range(m)]

        queue = []
        directions = [(-1,0),(1,0),(0,1),(0,-1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    building += 1
                    queue.append((i,j,0))
                    marked = [[False]*n for _ in range(m)]
                    while queue:
                        x,y,s = queue.pop(0)
                        for dx,dy in directions:
                            if 0<=x+dx<m and 0<=y+dy<n and grid[x+dx][y+dy] == 0 and not marked[x+dx][y+dy]:
                                marked[x+dx][y+dy] = True
                                count[x+dx][y+dy] += 1
                                dist[x+dx][y+dy] += s+1
                                queue.append((x+dx,y+dy,s+1))

        res = float('inf')

        for i in range(m):
            for j in range(n):
                if count[i][j] == building:
                    res = min(res,dist[i][j])

        return res if res!=float('inf') else -1
