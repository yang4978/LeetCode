class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        def check_result(num):
            res = 0
            i, j = n-1, 0
            while i >= 0 and j < n:
                if matrix[i][j] <= num:
                    res += i + 1
                    j += 1
                else:
                    i -= 1
            
            return res >= k

        left, right = matrix[0][0], matrix[-1][-1]

        while left < right:
            mid = (left+right)//2
            if check_result(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
