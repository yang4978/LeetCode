class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        sums = collections.defaultdict(int)
        s = 0
        res = 0
        for n in nums:
            sums[s] += 1
            s += n
            res += sums[s - goal] 
        
        return res
