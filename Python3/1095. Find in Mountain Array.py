# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def find_peak(self, mountain_arr, length):
        left = 0
        right = length - 1

        while left < right:
            mid = (left+right)//2
            if mountain_arr.get(mid-1) < mountain_arr.get(mid):
                left = mid + 1
            else:
                right = mid

        return mid
        # left = 0
        # right = length - 1

        # while left < right:
        #     mid = (left+right)//2
        #     l = mountain_arr.get(mid - 1)
        #     m = mountain_arr.get(mid)
        #     r = mountain_arr.get(mid + 1)

        #     if l < m and m > r:
        #         return mid
        #     elif r > m:
        #         left = mid + 1
        #     else:
        #         right = mid

        # return mid

    def binary_search(self, l, r, target, flag, mountain_arr, length):
        while l < r:
            mid = (l+r)//2
            temp = mountain_arr.get(mid) if flag>0 else mountain_arr.get(length-1-mid)

            if temp == target:
                return mid if flag>0 else length - mid - 1
            elif temp < target:
                l = mid + 1
            else:
                r = mid
        
        return l if flag>0 else length - l - 1

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()

        peak = self.find_peak(mountain_arr, length)

        res = self.binary_search(0, peak, target, 1, mountain_arr, length)

        if mountain_arr.get(res) != target:
            res = self.binary_search(0, peak, target, -1, mountain_arr, length)
        else:
            return res

        return res if target == mountain_arr.get(res) else -1
