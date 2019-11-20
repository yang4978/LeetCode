class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        if m==0:
            return
        n = len(matrix[0])

        self.temp = matrix.copy()
        for i in range(m):
            for j in range(n):
                self.temp[i][j] = self.temp[i][j] + (i>0)*self.temp[i-1][j] + (j>0)*self.temp[i][j-1] - (i>0 and j>0)*self.temp[i-1][j-1]

        # print(*self.temp,sep='\n')
        # print('\n')
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.temp[row2][col2] - (row1>=1)*self.temp[row1-1][col2] - (col1>=1)*self.temp[row2][col1-1] + (row1>=1 and col1>=1)*self.temp[row1-1][col1-1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
