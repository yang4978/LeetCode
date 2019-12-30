class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = [float("inf")]
        res = 0
        for num in arr:
            while stack and stack[-1]<=num:
                mid = stack.pop()
                res += mid*min(stack[-1],num)
            stack.append(num)
        while len(stack)>2:
            res += stack.pop()*stack[-1]
        
        return res

        # n = len(arr)
        # dp = [[float('inf')]*n for _ in range(n)]
        # max_ij = [[0]*n for _ in range(n)]
        # for i in range(n):
        #     for j in range(i,n):
        #         max_ij[i][j] = max(max_ij[i][j-1],arr[j])
        
        # for i in range(n):
        #     dp[i][i] = 0
        
        # for length in range(1,n):
        #     for start in range(n-length):
        #         for mid in range(start,start+length):
        #             dp[start][start+length] = min(dp[start][start+length],max_ij[start][mid]*max_ij[mid+1][start+length]+dp[start][mid]+dp[mid+1][start+length])
        
        # return dp[0][n-1]
