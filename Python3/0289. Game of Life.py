class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                num = 0
                for x in range(max(0,i-1),min(i+2,m)):
                    for y in range(max(0,j-1),min(j+2,n)):
                        num += int(board[x][y]>0) if (x != i or y != j) else 0

                if board[i][j] == 0:
                    if num == 3:
                        board[i][j] = -1
                else:
                    if num < 2 or num > 3:
                        board[i][j] = 2
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 1
                elif board[i][j] == 2:
                    board[i][j] = 0
