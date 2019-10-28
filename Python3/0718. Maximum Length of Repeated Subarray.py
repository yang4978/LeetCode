class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        la = len(A)
        lb = len(B)
        dp = [[0]*(1+lb) for i in range(la+1)]
        for i in range(la):
            for j in range(lb):
                if(A[i]==B[j]):
                    dp[i+1][j+1] = dp[i][j]+1

        return max(max(i) for i in dp)
