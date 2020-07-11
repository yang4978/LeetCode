class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = []
        temp = []
        l = len(nums)

        for i in range(l-1,-1,-1):
            left = 0
            right = l-1-i

            while left<right:
                mid = (left+right)//2
                if temp[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid
            res.append(left)
            temp.insert(left,nums[i])
        
        return reversed(res)
