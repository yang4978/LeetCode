class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # arr = [-float('inf')]+nums+[float('inf')]
        # flag = 0
        # i = 1
        # l = len(nums)
        # while i < l:
        #     if arr[i-1]<=arr[i]<=arr[i+1]:
        #         i += 1
        #     else:
        #         if arr[:i-1] + arr[i:] == sorted(arr[:i-1] + arr[i:]) or arr[:i] + arr[i+1:] == sorted(arr[:i] + arr[i+1:]) or arr[:i+1] + arr[i+2:] == sorted(arr[:i+1] + arr[i+2:]):
        #             return True
        #         else:
        #             return False
        # return True 

        count = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                count += 1
                if count > 1:
                    return False
                if i > 0 and nums[i+1] < nums[i-1]:
                    nums[i+1] = nums[i]
        
        return True
