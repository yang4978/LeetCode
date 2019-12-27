class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == [] or matrix[0]==[]:
            return False

        m = len(matrix)
        n = len(matrix[0])
        if matrix == [] or matrix[0]==[]:
            return False
        
        l = 0
        r = m*n-1
        while l<=r:
            mid = l + (r-l)//2
            if matrix[mid//n][mid%n] == target:
                return True
            elif matrix[mid//n][mid%n] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False

        # if matrix == [] or matrix[0]==[]:
        #     return False

        # m = len(matrix)
        # n = len(matrix[0])

        # row_l = 0
        # row_r = m - 1

        # while row_l<=row_r:
        #     row_m = row_l + (row_r-row_l)//2
        #     if matrix[row_m][0]>target:
        #         row_r = row_m - 1
        #     else:
        #         row_l = row_m + 1

        # row_l = row_l - 1
        # col_l = 0
        # col_r = n - 1
        
        # while col_l<=col_r:
        #     col_m = col_l + (col_r-col_l)//2
        #     if matrix[row_l][col_m]==target:
        #         return True
        #     elif matrix[row_l][col_m]>target:
        #         col_r = col_m - 1
        #     else:
        #         col_l = col_m + 1

        # return False

        # if matrix == [] or matrix[0]==[]:
        #     return False

        # m = len(matrix)
        # n = len(matrix[0])

        # row_l = 0
        # row_r = m

        # while row_r-row_l!=1 and row_r!=row_l:
        #     row_m = row_l + (row_r-row_l)//2
        #     if matrix[row_m][0]>target:
        #         row_r = row_m
        #     else:
        #         row_l = row_m

        # col_l = 0
        # col_r = n
        # temp = -1
        
        # while 1:
        #     col_m = col_l + (col_r-col_l)//2
        #     if temp==col_m:
        #         break
        #     temp = col_m
        #     if matrix[row_l][col_m]==target:
        #         return True
        #     elif matrix[row_l][col_m]>target:
        #         col_r = col_m
        #     else:
        #         col_l = col_m

        # return False
