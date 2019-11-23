# class Solution:
#     def maxKilledEnemies(self, grid: List[List[str]]) -> int:
#         m = len(grid)
#         if m==0:
#             return 0
#         n = len(grid[0])
#         if n==0:
#             return 0

#         dp1 = [[0]*(1+n) for _ in range(1+m)] #rows
#         dp2 = [[0]*(1+n) for _ in range(1+m)] #cols

#         for i in range(1,1+m):
#             for j in range(1,1+n):
#                 if grid[i-1][j-1] == 'W':
#                     dp1[i][j] = -1
#                     dp2[i][j] = -1
                
#                 elif grid[i-1][j-1] == '0':
#                     dp1[i][j] = max(0,dp1[i][j-1])
#                     dp2[i][j] = max(0,dp2[i-1][j])
                
#                 else:
#                     dp1[i][j] = max(0,dp1[i][j-1]) + 1
#                     k = j-1
#                     while k>0 and dp1[i][k]!=-1:
#                         dp1[i][k] = dp1[i][k] + 1
#                         k -= 1

#                     dp2[i][j] = max(0,dp2[i-1][j]) + 1
#                     k = i-1
#                     while k>0 and dp2[k][j]!=-1:
#                         dp2[k][j] = dp2[k][j] + 1
#                         k -= 1

#         res_list = [dp1[i][j]+dp2[i][j] for i in range(1+m) for j in range(1+n) if grid[i-1][j-1]!='E']
#         return max(res_list) if res_list!=[] else 0
                

        
        
class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        res = 0
        def count(x0, y0):
            cnt = 0
            for x in range(x0, -1, -1): #向上
                if grid[x][y0] == "E":
                    cnt += 1
                elif grid[x][y0] == "W":
                    break
                    
            for x in range(x0, m):  #向下
                if grid[x][y0] == "E":
                    cnt += 1
                elif grid[x][y0] == "W":
                    break
                    
            for y in range(y0, -1, -1): #向左
                if grid[x0][y] == "E":
                    cnt += 1
                elif grid[x0][y] == "W":
                    break      
                     
            for y in range(y0, n): #向右
                if grid[x0][y] == "E":
                    cnt += 1
                elif grid[x0][y] == "W":
                    break   
                    
            return cnt
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    res = max(res, count(i, j))
        return res
