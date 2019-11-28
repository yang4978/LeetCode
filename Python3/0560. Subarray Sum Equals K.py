class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        digit = {0:1}
        res = 0
        s = 0

        for n in nums:
            s += n
            if s-k in digit:
                res += digit[s-k]
            if s in digit:
                digit[s] += 1
            else:
                digit[s] = 1

        
        return res
