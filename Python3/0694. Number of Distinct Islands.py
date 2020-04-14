class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m = len(grid)

        if not m:
            return 0
        
        n = len(grid[0])

        block = set()

        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    queue = [(i,j)]
                    grid[i][j] = 0
                    s = ''

                    while queue:
                        x,y = queue.pop(0)
                        for dx,dy in directions:
                            if 0<=x+dx<m and 0<=y+dy<n and grid[x+dx][y+dy]:
                                grid[x+dx][y+dy] = 0
                                queue.append((x+dx,y+dy))
                                s += str(x+dx-i)+str(y+dy-j)
                    block.add(s)
        return len(block)
