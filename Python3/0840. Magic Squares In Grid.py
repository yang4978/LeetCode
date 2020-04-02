class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0

        for i in range(1,m-1):
            for j in range(1,n-1):
                if grid[i][j] == 5:
                    s = set([grid[x][y] for x in range(i-1,i+2) for y in range(j-1,j+2)])
                    if len(s) == 9 and max(s) == 9 and min(s) == 1 and sum(grid[i-1][j-1:j+2]) == 15 and sum(grid[i+1][j-1:j+2]) == 15 and sum(grid[i][j-1:j+2]) == 15 and grid[i-1][j-1]+grid[i][j-1]+grid[i+1][j-1] == 15 and grid[i-1][j]+grid[i][j]+grid[i+1][j] == 15 and grid[i-1][j+1]+grid[i][j+1]+grid[i+1][j+1] == 15:
                        res += 1
        
        return res
