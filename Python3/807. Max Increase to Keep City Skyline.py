class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        #n = len(grid)
        #xmax = [max(grid[i]) for i in range(n)]
        #ymax = [max([grid[i][j] for i in range(n)]) for j in range(n)]
        #return sum(min(xmax[i], ymax[j]) - grid[i][j] for i in range(n) for j in range(n))

        xmax = list(map(max, grid))
        ymax = list(map(max, zip(*grid)))
        return sum(min(xmax[i], ymax[j]) - h for i, row in enumerate(grid) for j, h in enumerate(row))
