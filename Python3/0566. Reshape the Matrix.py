class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(nums)
        if m == 0:
            return nums
        n = len(nums[0])

        if r*c != m*n:
            return nums

        res = [[0]*c for _ in range(r)]

        for i in range(m):
            for j in range(n):
                index = n*i + j
                res[index//c][index%c] = nums[i][j]
        
        return res
