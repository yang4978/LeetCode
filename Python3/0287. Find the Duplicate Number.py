class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 1
        right = len(nums)-1

        while left<right:
            mid = left + (right-left)//2
            temp = 0
            for i in nums:
                temp += (i<=mid)
            if temp<=mid:
                left = mid + 1
            else:
                right = mid
        return left
