class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0

        l = len(nums)
        left,right = 0,0
        res = 0
        temp = 1

        while right<l:
            temp *= nums[right]

            while temp>=k:
                temp //= nums[left]
                left += 1
            res += right-left+1
            right += 1

        return res

        # l = len(nums)
        # left,right = 0,0
        # res = []
        # temp = 1

        # while right<l:
        #     temp *= nums[right]
        #     if temp<k and (right+1<l and temp*nums[right+1]>=k):
        #         res.append((left,right))
        #     if temp>=k:
        #         while left<right and temp>=k:
        #             temp //= nums[left]
        #             left += 1
        #             if temp<k and (right+1<l and temp*nums[right+1]>=k):
        #                 res.append((left,right))
        #     right += 1
        # if temp<k:
        #     res.append((left,right-1))

        # ans = 0
        # for i,j in res:
        #     ans += (j-i+1)*(j-i+2)//2
        
        # for i in range(len(res)-1):
        #     if res[i+1][0]<=res[i][1]:
        #         ans -= (res[i][1]-res[i+1][0]+1)*(res[i][1]-res[i+1][0]+2)//2

        # return ans
