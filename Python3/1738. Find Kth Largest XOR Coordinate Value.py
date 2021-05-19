class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        arr = [[0]*n for _ in range(m)]

        arr[0][0] = matrix[0][0]
        res = [matrix[0][0]]

        for i in range(1, m):
            t = matrix[i][0] ^ arr[i - 1][0]
            arr[i][0] = t
            res.append(t)
        
        for j in range(1, n):
            t = matrix[0][j] ^ arr[0][j - 1]
            arr[0][j] = t
            res.append(t)

        for i in range(1, m):
            for j in range(1, n):
                t = matrix[i][j] ^ arr[i - 1][j] ^ arr[i][j - 1] ^ arr[i - 1][j - 1]
                arr[i][j] = t
                res.append(t)
                
        return sorted(res)[-k]
