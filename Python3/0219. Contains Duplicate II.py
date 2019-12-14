class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = len(nums)
        s = set()
        for i in range(l):
            if nums[i] in s:
                return True
            
            s  |= {nums[i]}

            if len(s)>k:
                s -= {nums[i-k]}
        
        return  False
