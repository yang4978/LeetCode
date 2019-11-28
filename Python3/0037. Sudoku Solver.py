class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        block = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    block[i//3*3+j//3].add(board[i][j])
        
        def dfs(i,j,board,row,col,block):
            while(board[i][j]!='.'):
                j += 1
                if j==9:
                    i += 1
                    j = 0
                if i==9:
                    return True
            
            for num in range(1,10):
                n = str(num)
                if n not in row[i] and n not in col[j] and n not in block[i//3*3+j//3]:
                    board[i][j] = n
                    row[i].add(n)
                    col[j].add(n)
                    block[i//3*3+j//3].add(n)
                    if dfs(i,j,board,row,col,block) == True:
                        return True
                    else:
                        board[i][j] = '.'
                        row[i].remove(n)
                        col[j].remove(n)
                        block[i//3*3+j//3].remove(n)

            return False
        
        dfs(0,0,board,row,col,block)
