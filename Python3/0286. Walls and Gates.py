class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        if not rooms:
            return

        m = len(rooms)
    
        n = len(rooms[0])

        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        queue = collections.deque()

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i,j))

        while queue:
            x, y = queue.popleft()
            for dx,dy in directions:
                if 0<=x+dx<m and 0<=y+dy<n and rooms[x+dx][y+dy]==2147483647:
                    rooms[x+dx][y+dy] = rooms[x][y]+1
                    queue.append((x+dx,y+dy))

        # m = len(rooms)
        
        # if m == 0:
        #     return rooms
        
        # n = len(rooms[0])

        # directions = [(0,1),(1,0),(0,-1),(-1,0)]

        # for i in range(m):
        #     for j in range(n):
        #         if rooms[i][j] == 0:
        #             queue = collections.deque()
        #             queue.append((i,j))
        #             while queue:
        #                 x, y = queue.popleft()
        #                 for dx,dy in directions:
        #                     if 0<=x+dx<m and 0<=y+dy<n and rooms[x+dx][y+dy]>rooms[x][y]+1:
        #                         rooms[x+dx][y+dy] = rooms[x][y]+1
        #                         queue.append((x+dx,y+dy))
