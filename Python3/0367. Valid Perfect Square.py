class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num<2:
            return True

        left = 0
        right = num

        while left<right:
            mid = (left+right)>>1
            res = mid*mid

            if res == num:
                return True
            
            elif res < num:
                left = mid + 1
            
            else:
                right = mid
        
        return False

        # if num<2:
        #     return True

        # left = 0
        # right = num//2

        # while left<=right:
        #     mid = (left+right)>>1
        #     res = mid*mid

        #     if res == num:
        #         return True
            
        #     elif res < num:
        #         left = mid + 1
            
        #     else:
        #         right = mid - 1
        
        # return False
