class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(list)
        col = collections.defaultdict(list)
        block = collections.defaultdict(list)

        for i in range(9):
            for j in range(9):
                if(board[i][j]=='.'):
                    continue
                if (board[i][j] not in row[i]
                and board[i][j] not in col[j]
                and board[i][j] not in block[j//3+i//3*3]):
                    row[i].append(board[i][j])
                    col[j].append(board[i][j])
                    block[j//3+i//3*3].append(board[i][j])

                else:                    
                    return False
        
        return True
