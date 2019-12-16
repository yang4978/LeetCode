class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        diff = (n+1)*n//2 - sum(nums)
        digit = set()
        for i in nums:
            if i not in digit:
                digit |= {i}
            else:
                return [i,i+diff]
