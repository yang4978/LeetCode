class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        # m = len(A)
        # n = len(A[0])
        # res = 0
        # for i in range(m):
        #     before = sum(2**(n-1-j) for j in range(n) if A[i][j])
        #     after = 2**n - before - 1
        #     if after > before:
        #         for j in range(n):
        #             A[i][j] = 1 - A[i][j]
        #         res += after
        #     else:
        #         res += before
        
        # for j in range(n):
        #     before = sum(1 for i in range(m) if A[i][j])
        #     after = m - before
        #     if after > before:
        #         res += (after - before)*2**(n-1-j)

        # return res

        m, n = len(A), len(A[0])

        for i in range(m):
            if A[i][0] == 0:
                for j in range(n):
                    A[i][j] ^= 1
        
        res = m * 2**(n-1)

        for j in range(1,n):
            count = sum(A[i][j] for i in range(m))
            res += max(m-count,count) * 2**(n-1-j)
        
        return res
