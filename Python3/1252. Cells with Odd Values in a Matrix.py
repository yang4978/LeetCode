class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        row = [0]*n
        col = [0]*m

        for i,j in indices:
            row[i] += 1
            col[j] += 1
        
        x = sum(r%2 for r in row)
        y = sum(c%2 for c in col)

        return x*(m-y)+y*(n-x)
