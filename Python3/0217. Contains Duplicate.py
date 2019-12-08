class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        digit = {}

        for i in nums:
            if i not in digit:
                digit[i] = 1
            else:
                return True
        
        return False

