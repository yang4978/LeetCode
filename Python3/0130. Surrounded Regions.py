class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def expansion(i,j):
            for di,dj in {(-1,0),(1,0),(0,-1),(0,1)}:
                if -1<i+di<m and -1<j+dj<n and state[i+di][j+dj]=='O':
                    return True
            return False

        if not board:
            return board

        m = len(board)
        n = len(board[0])  
        state = [['X']*n for _ in range(m)]

        for j in range(n):
            state[0][j] = board[0][j]
            state[m-1][j] = board[m-1][j]
        
        for i in range(m):
            state[i][0] = board[i][0]
            state[i][n-1] = board[i][n-1]
        
        flag = 1

        while flag:
            flag = 0

            for k in range(1, (1+min(m,n))//2):
                for j in range(k,n-k):
                    if board[k][j]=='O' and state[k][j] == 'X' and expansion(k,j):
                        state[k][j] = 'O'
                        flag = 1
                    
                    if board[m-1-k][j]=='O' and state[m-1-k][j] == 'X' and expansion(m-1-k,j):
                        state[m-1-k][j] = 'O'
                        flag = 1
                
                for i in range(k,m-k):
                    if board[i][k]=='O' and state[i][k] == 'X' and expansion(i,k):
                        state[i][k] = 'O'
                        flag = 1
                    
                    if board[i][n-1-k]=='O' and state[i][n-1-k] == 'X' and expansion(i,n-1-k):
                        state[i][n-1-k] = 'O'
                        flag = 1

        board[:] = state[:]
