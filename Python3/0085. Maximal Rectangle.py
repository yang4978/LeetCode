class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if(matrix==[]):
            return 0
            
        m = len(matrix)
        n = len(matrix[0])

        res = 0
        height = [0]*n
        stack = [-1]

        for i in range(m):
            for j in range(n):
                if(matrix[i][j]=='1'):
                    height[j] += 1
                else:
                    height[j] = 0
                while(stack[-1]!=-1 and height[j]<height[stack[-1]]):
                    res = max(res,height[stack.pop()]*(j-1-stack[-1]))
                stack.append(j)
            while(stack[-1]!=-1):
                res = max(res,height[stack.pop()]*(n-1-stack[-1]))
        
        return res

