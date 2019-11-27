class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def searchLeft(nums,target):
            l = 0
            r = len(nums) - 1
            while(l<=r):
                m = l + (r-l)//2
                if nums[m] == target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
            return l if l<=len(nums)-1 and nums[l]==target else -1

        def searchRight(nums,target):
            l = 0
            r = len(nums) - 1
            while(l<=r):
                m = l + (r-l)//2
                if nums[m] == target:
                    l = m + 1
                elif nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
            return r if r>=0 and nums[r] == target else -1

        return [searchLeft(nums,target),searchRight(nums,target)]

    # def binarySearch(self,nums,target):
    #     l = 0
    #     r = len(nums)-1
    #     while(l<=r):
    #         m = (l+r)//2
    #         if nums[m]==target:
    #             return m
    #         elif nums[m]>target:
    #             r = m-1
    #         else:
    #             l = m+1
        
    #     return -1

    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    #     m = self.binarySearch(nums,target)
    #     if m==-1:
    #         return [-1,-1]
        
    #     l = r = m
        
    #     lt = 0
    #     rt = 0

    #     while(lt!=-1 or rt!=-1):
        
    #         lt = self.binarySearch(nums[:l],target)
    #         l = lt if lt!=-1 else l

    #         if m+1<=len(nums)-1:
    #             rt = self.binarySearch(nums[r+1:],target) 
    #         else:
    #             rt = -1

    #         r = rt+r+1 if rt!=-1 else r
        
    #     return [l,r]
