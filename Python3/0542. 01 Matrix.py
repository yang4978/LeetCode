class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        res = [[float('inf')]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0 and res[i][j]!=0:
                    queue = [(i,j)]
                    res[i][j] = 0
                    while queue:
                        x,y = queue.pop(0)
                        step = res[x][y]                  
                        for dx,dy in directions:
                            new_x = x + dx
                            new_y = y + dy
                            if 0<=new_x<m and 0<=new_y<n:
                                if matrix[new_x][new_y] == 0 and res[new_x][new_y]!=0:
                                    res[new_x][new_y] = 0
                                    queue.append((new_x,new_y))
                                elif matrix[new_x][new_y] and res[new_x][new_y]>1+step:
                                    res[new_x][new_y] = step+1
                                    queue.append((new_x,new_y))

        return res
