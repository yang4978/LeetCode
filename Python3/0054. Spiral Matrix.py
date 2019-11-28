class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix ==[]:
            return []
        res = []
        m = len(matrix)
        n = len(matrix[0])

        for k in range((min(m,n)+1)//2):
            for j in range(k,n-k):
                res.append(matrix[k][j])
            print(res)

            for i in range(k+1,m-k):
                res.append(matrix[i][n-k-1])
            print(res)

            for j in range(n-k-2,k-1,-1):
                if k==m-k-1:
                    continue
                res.append(matrix[m-k-1][j])
            print(res)
            for i in range(m-k-2,k,-1):
                if k==n-k-1:
                    continue
                res.append(matrix[i][k])
            print(res)
        return res
