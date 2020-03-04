class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        oranges = 0
        queue = []

        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    oranges += 1
                elif grid[i][j] == 2:
                    queue.append((i,j))
        
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        t = 0

        while queue and oranges:
            t += 1
            for _ in range(len(queue)):
                x, y = queue.pop(0)
                for dx, dy in directions:
                    if 0<=dx+x<m and 0<=dy+y<n and grid[x+dx][y+dy] == 1:
                        grid[x+dx][y+dy] = 2
                        oranges -= 1
                        queue.append((x+dx,y+dy))

        return -1 if oranges else t
