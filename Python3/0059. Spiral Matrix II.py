class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0]*n for _ in range(n)]

        num = 1
        for k in range((n+1)//2):
            for j in range(k,n-k):
                res[k][j] = num
                num += 1
            
            for i in range(k+1,n-k):
                res[i][n-k-1] = num
                num += 1
            
            for j in range(n-k-2,k-1,-1):
                res[n-k-1][j] = num
                num += 1
            
            for i in range(n-k-2,k,-1):
                res[i][k] = num
                num += 1
            
        return res
