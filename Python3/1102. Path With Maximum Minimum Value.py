from heapq import *

class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        m = len(A)
        n = len(A[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        visited = set((0,0))

        queue = [(-A[0][0],0,0)]

        heapify(queue)

        while queue:
            score,x,y = heappop(queue)
            if x==m-1 and y==n-1:
                    return -score
            
            for dx,dy in directions:
                nx = x + dx
                ny = y + dy
                
                if 0<=nx<m and 0<=ny<n and (nx,ny) not in visited:
                    visited.add((nx,ny))
                    heappush(queue,(max(score,-A[nx][ny]),nx,ny))

