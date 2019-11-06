class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        x = len(grid)
        y = len(grid[0])
        res = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res += (2+4*grid[i][j]) if grid[i][j] else 0
                if(i<x-1):
                    res -= 2*min(grid[i][j],grid[i+1][j])
                if(j<y-1):
                    res -= 2*min(grid[i][j],grid[i][j+1])                    
        return res
#         x = len(grid)
#         y = len(grid[0])
#         res = 0
        
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 res += (2+4*grid[i][j]) if grid[i][j] else 0
#                 if(i>0):
#                     res -= min(grid[i][j],grid[i-1][j])
#                 if(i<x-1):
#                     res -= min(grid[i][j],grid[i+1][j])
#                 if(j>0):
#                     res -= min(grid[i][j],grid[i][j-1])
#                 if(j<y-1):
#                     res -= min(grid[i][j],grid[i][j+1])
                    
#         return res
