class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)

        if not m:
            return 0

        n = len(grid[0])

        row = []
        col = []
        l = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    row.append(i)
                    col.append(j)
                    l += 1

        col.sort()
        x = row[l//2]
        y = col[l//2]

        res = 0
        for i in row:
            res += abs(i-x)
        for j in col:
            res += abs(j-y)
        
        return res

