class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return [ [A[i][j] for i in range(len(A))] for j in range(len(A[0]))]

        # m = len(A)
        # n = len(A[0])
        # res = [[0]*m for _ in range(n)]

        # for i in range(m):
        #     for j in range(n):
        #         res[j][i] = A[i][j]
        
        # return res
