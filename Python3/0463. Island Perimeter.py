class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0 
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res += 4 
                    if (i>0):
                        res -= grid[i-1][j] 
                    if (i+1<m):
                        res -= grid[i+1][j] 
                    if (j>0):
                        res -= grid[i][j-1]  
                    if (j+1<n):
                        res -= grid[i][j+1]
        
        return res
