class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        
        hashMap = {}
        res = 0

        nums.sort(reverse=True)

        for i in nums:
            if i+k in hashMap and hashMap[i+k]:
                res += 1
                hashMap[i+k] = False
            
            if i not in hashMap:
                hashMap[i] = True
        
        return res
             

        # if k < 0:
        #     return 0
        # if k == 0:
        #     return len(set([i for i in nums if nums.count(i)>=2]))
        # cl = [i+k for i in nums]
        # return len(set(cl)&set(nums))


        # if k<0:
        #     return 0
        # nums.sort()
        # res = []
        # l = len(nums)
        # for i in range(l):
        #     if nums[i] not in res and nums[i]+k in nums[i+1:]:
        #         res.append(nums[i])
        
        # return len(res)

        # if k<0:
        #     return 0
        # set_num = set(nums)
        # if k==0:
        #     return sum(1 for i in set_num if nums.count(i)>1)
        # else:
        #     nums = list(set_num)
            
        #     return sum(1 for i in nums if i+k in nums)
