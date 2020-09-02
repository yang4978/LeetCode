class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def cal_digt(n):
            res = 0
            while n:
                res += n%10
                n //= 10
            return res

        directions = [(1,0),(0,1)]
        used =  [[0]*n for _ in range(m)]
        used[0][0] = 1
        queue = [(0,0)]

        grid = 1
        while queue:
            x, y = queue.pop(0)
            for dx,dy in directions:
                if 0<=x+dx<m and 0<=y+dy<n and used[x+dx][y+dy]==0 and cal_digt(x+dx)+cal_digt(y+dy)<=k:
                    grid += 1
                    queue.append((x+dx,y+dy))
                    used[x+dx][y+dy] = 1
        
        return grid
