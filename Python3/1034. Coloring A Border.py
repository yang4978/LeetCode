class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        stack = [(r0,c0)]
        original = grid[r0][c0]
        if original == color:
            return grid
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        res = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                res[i][j] = grid[i][j]

        while stack:
            x,y = stack.pop(0)
            grid[x][y] = 0

            if (x>0 and grid[x-1][y]!=original and grid[x-1][y]!=0) or (x<m-1 and grid[x+1][y]!=original and grid[x+1][y]!=0) or (y>0 and grid[x][y-1]!=original and grid[x][y-1]!=0) or (y<n-1 and grid[x][y+1]!=original and grid[x][y+1]!=0) or x==0 or x==m-1 or y==0 or y==n-1:
                res[x][y] = color

            for dx,dy in directions:
                if 0<=x+dx<m and 0<=y+dy<n and grid[x+dx][y+dy] == original:
                    stack.append((x+dx,y+dy))

        return res
