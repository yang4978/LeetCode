class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        if(n<=1): return -1
        res = 0
        i = 0
        j = n-1
        while(i<j):
            res = max(res,(j-i)*min(height[i],height[j]))
            if(height[i]<height[j]):
                i += 1
            else:
                j -= 1
        return res
