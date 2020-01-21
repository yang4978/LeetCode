class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        l = len(nums)
        perimeter = sum(nums)
        side = perimeter//4

        if side*4!=perimeter:
            return False
        
        def dfs(index):
            if index == l:
                return sums[0] == sums[1] == sums[2] == possible
