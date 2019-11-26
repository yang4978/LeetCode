class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_pivot(l,r):
            if(nums[l]<nums[r]):
                return 0

            while(l<=r):
                pivot = (l+r)//2
                if nums[pivot]<nums[pivot-1]:
                    return pivot

                if nums[pivot]>nums[r]:
                    l = pivot+1
                else:
                    r = pivot-1
        
        n = len(nums)

        if nums==[]:
            return -1
        
        if n==1:
            return 0 if nums[0]==target else -1

        pivot = find_pivot(0,n-1)
        
        if nums[n-1]>=target:
            l = pivot
            r = n-1
        else:
            l = 0
            r= pivot

        while(l<=r):
            m = (l+r)//2
            if nums[m]==target:
                return m
            elif nums[m]>target:
                r = m-1
            else:
                l = m+1
        return -1
