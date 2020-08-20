class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        # if board[click[0]][click[1]] == 'M':
        #     board[click[0]][click[1]] = 'X'
        #     return board

        # directions = [(0,-1),(0,1),(-1,0),(1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
        # m = len(board)
        # n = len(board[0])

        # count = [[0]*n for _ in range(m)]

        # for i in range(m):
        #     for j in range(n):
        #         if board[i][j] == 'M':
        #             count[i][j] = -1
        #             for dx,dy in directions:
        #                 if 0<=i+dx<m and 0<=j+dy<n and count[i+dx][j+dy]!=-1:
        #                     count[i+dx][j+dy] += 1

        # block = [click]

        # while block:
        #     x, y = block.pop(0)
        #     if board[x][y] == 'E':
        #         if count[x][y] != 0:
        #             board[x][y] = str(count[x][y])
        #         else:
        #             board[x][y] = 'B'
        #             for dx,dy in directions:
        #                 if 0<=x+dx<m and 0<=y+dy<n:
        #                     block.append([x+dx,y+dy])
    
        # return board

        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        directions = [(0,-1),(0,1),(-1,0),(1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
        m = len(board)
        n = len(board[0])

        used = [[0]*n for i in range(m)]

        block = [click]

        while block:
            x, y = block.pop(0)
            if board[x][y] == 'E':
                count = 0
                points = [[x+dx,y+dy] for dx,dy in directions if 0<=x+dx<m and 0<=y+dy<n]
                for xx, yy in points:
                    count += 1 if board[xx][yy] == 'M' else 0
                        
                if count>0:
                    board[x][y] = str(count)
                else:
                    board[x][y] = 'B'
                    for xx, yy in points:
                        if used[xx][yy] == 0:
                            block.append([xx,yy])
                            used[xx][yy] = 1
    
        return board
