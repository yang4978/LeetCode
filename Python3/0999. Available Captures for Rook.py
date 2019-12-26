class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    x = i
                    y = j
                    break
        
        s1 = ''.join(board[x][:]).replace('.','')
        s2 = ''.join([board[i][y] for i in range(8)]).replace('.','')
        return int('pR' in s1) + int('Rp' in s1) + int('pR' in s2) + int('Rp' in s2)

        # for i in range(8):
        #     for j in range(8):
        #         if board[i][j] == 'R':
        #             x = i
        #             y = j
        #             break

        # res = 0

        # for i in range(x-1,-1,-1):
        #     if board[i][y] == 'B':
        #         break
        #     if board[i][y] == 'p':
        #         res += 1
        #         break
        
        # for i in range(x+1,8):
        #     if board[i][y] == 'B':
        #         break
        #     if board[i][y] == 'p':
        #         res += 1
        #         break

        # for j in range(y-1,-1,-1):
        #     if board[x][j] == 'B':
        #         break
        #     if board[x][j] == 'p':
        #         res += 1
        #         break

        # for j in range(y+1,8):
        #     if board[x][j] == 'B':
        #         break
        #     if board[x][j] == 'p':
        #         res += 1
        #         break
        
        # return res
